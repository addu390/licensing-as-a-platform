from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from . import cache_views
from .constants import LICENSE, PLAN, STATUS, ACTIVATION_DATE, EXPIRY_DATE, TYPE, FEATURE, PRICE, NAME, DESCRIPTION

from core.models import Plan, License, Feature
from rest_framework import status
from core.serializers import FeaturePlanSerializer, LicenseSerializer, LicensePlanSerializer, PlanSerializer, FeatureSerializer
from licensing_platform.settings import TIME_ZONE
from django.db import transaction, IntegrityError
from rest_framework.response import Response
from datetime import datetime, timedelta
import pytz


class CreatePlan(APIView):
    def post(self, request):
        feature_id = request.data.get(FEATURE)
        plan_name = request.data.get(NAME)
        plan_status = request.data.get(STATUS)
        plan_type = request.data.get(TYPE)
        plan_price = request.data.get(PRICE)
        plan_description = request.data.get(DESCRIPTION)

        feature_object = get_object_or_404(Feature, external_id=feature_id)
        print(feature_object)
        feature_data = FeatureSerializer(feature_object).data
        plan_data = {
            NAME: plan_name,
            STATUS: plan_status,
            TYPE: plan_type,
            PRICE: plan_price,
            DESCRIPTION: plan_description
        }
        plan_serializer = PlanSerializer(
            data=plan_data, remove=['id', 'created_at', 'updated_at'])
        if plan_serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    plan_object = plan_serializer.save()
                    plan_feature_data = {
                        FEATURE: feature_data['external_id'],
                        PLAN: plan_object,
                    }
                    plan_feature_serializer = FeaturePlanSerializer(
                        data=plan_feature_data)
                    if plan_feature_serializer.is_valid():
                        plan_feature_serializer.save()
                    return Response(plan_serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateLicense(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        plan_id = request.data.get(PLAN)
        license_status = request.data.get(STATUS)
        utc = pytz.timezone(TIME_ZONE)

        plan_object = get_object_or_404(Plan, external_id=plan_id)
        plan_data = PlanSerializer(plan_object).data
        license_data = {
            STATUS: license_status,
            ACTIVATION_DATE: datetime.now(utc),
            # Change this based on the Package.
            EXPIRY_DATE: datetime.now(utc) + timedelta(days=365 * 1)
        }
        license_serializer = LicenseSerializer(
            data=license_data, remove=['id', 'created_at', 'updated_at'])
        if license_serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    license_object = license_serializer.save()

                    license_plan_data = {
                        PLAN: plan_data['external_id'],
                        LICENSE: license_object,
                    }
                    license_plan_serializer = LicensePlanSerializer(
                        data=license_plan_data)
                    if license_plan_serializer.is_valid(raise_exception=True):
                        license_plan_serializer.save()

                    update_license_cache(license_object.license_id)
                    return Response(license_serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(license_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LicenseDetails(APIView):
    def get(self, request, license_id):
        license_data = cache_views.get(license_id)
        if not license_data:
            license_data = update_license_cache(license_id)
        return Response(license_data)


class LicenseStatus(APIView):
    def put(self, request, license_id):
        license_object = get_object_or_404(License, license_id=license_id)
        serializer = LicenseSerializer(
            license_object, data=request.data, partial=True, fields=('status',))
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                update_license_cache(license_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, plan_id):
        plan_object = get_object_or_404(Plan, external_id=plan_id)
        serializer = PlanSerializer(plan_object)
        print(serializer.data['external_id'])
        return Response(serializer.data)


class FeatureDetails(APIView):
    def get(self, request, feature_id):
        feature_object = get_object_or_404(Feature, external_id=feature_id)
        serializer = FeatureSerializer(feature_object)
        return Response(serializer.data)


def update_license_cache(license_id):
    license_object = get_object_or_404(License, license_id=license_id)
    serializer = LicenseSerializer(license_object)
    license_data = dict(serializer.data)
    cache_views.update(license_id, license_data)
    return license_data


class PlanList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        plan_objects = Plan.objects.all()
        plan_serializer = PlanSerializer(plan_objects, many=True)
        return Response(plan_serializer.data, status=status.HTTP_200_OK)


class FeatureList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        feature_objects = Feature.objects.all()
        plan_serializer = FeatureSerializer(feature_objects, many=True)
        return Response(plan_serializer.data, status=status.HTTP_200_OK)

from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from . import cache_views
from .constants import LICENSE, PLAN, STATUS, ACTIVATION_DATE, EXPIRY_DATE

from core.models import Plan, License, Feature
from rest_framework import status
from core.serializers import LicenseSerializer, LicensePlanSerializer, PlanSerializer, FeatureSerializer
from licensing_platform.settings import TIME_ZONE
from django.db import transaction, IntegrityError
from rest_framework.response import Response
from datetime import datetime, timedelta
import pytz


class CreateLicense(APIView):
    def post(self, request):
        plan_id = request.data.get(PLAN)
        license_status = request.data.get(STATUS)
        utc = pytz.timezone(TIME_ZONE)

        plan_object = get_object_or_404(Plan, external_id=plan_id)
        license_data = {
            STATUS: license_status,
            ACTIVATION_DATE: datetime.now(utc),
            EXPIRY_DATE: datetime.now(utc) + timedelta(days=365 * 1)  # Change this based on the Package.
        }
        license_serializer = LicenseSerializer(data=license_data, remove=['id', 'created_at', 'updated_at'])
        if license_serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    license_object = license_serializer.save()

                    license_plan_data = {
                        PLAN: plan_object.external_id,
                        LICENSE: license_object.external_id,
                    }
                    license_plan_serializer = LicensePlanSerializer(data=license_plan_data)
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
        serializer = LicenseSerializer(license_object, data=request.data, partial=True, fields=('status',))
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                update_license_cache(license_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanDetails(APIView):
    def get(self, request, plan_id):
        plan_object = get_object_or_404(Plan, external_id=plan_id)
        serializer = PlanSerializer(plan_object)
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


class Health(APIView):
    def get(self, request):
        return HttpResponse("OK")

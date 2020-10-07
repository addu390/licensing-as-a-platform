from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .constants import ACTIVE, LICENSE, PACKAGE, STATUS, ACTIVATION_DATE, EXPIRY_DATE

from core.models import Package
from rest_framework import status
from core.serializers import LicenseSerializer, LicensePackageSerializer
from licensing_platform.settings import TIME_ZONE
from django.db import transaction
from rest_framework.response import Response
from datetime import datetime, timedelta
import pytz


class Create(APIView):

    def post(self, request):
        package_id = request.data.get(PACKAGE)
        license_status = request.data.get(STATUS)
        utc = pytz.timezone(TIME_ZONE)

        package_object = get_object_or_404(Package, external_id=package_id, status=ACTIVE)
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

                    license_package_data = {
                        PACKAGE: package_object.id,
                        LICENSE: license_object.id,
                    }
                    license_package_serializer = LicensePackageSerializer(data=license_package_data)
                    if license_package_serializer.is_valid(raise_exception=True):
                        license_package_serializer.save()
                    return Response(license_serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(license_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



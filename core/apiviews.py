from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

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
        package_id = request.data.get("package")
        license_status = request.data.get("status")
        utc = pytz.timezone(TIME_ZONE)

        package_object = get_object_or_404(Package, external_id=package_id, status="ACTIVE")
        license_data = {
            'status': license_status,
            'activation_date': datetime.now(utc),
            'expiry_date': datetime.now(utc) + timedelta(days=365 * 1)  # Change this based on the Package.
        }
        license_serializer = LicenseSerializer(data=license_data, remove=['id', 'created_at', 'updated_at'])
        if license_serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    license_object = license_serializer.save()

                    license_package_data = {
                        'package': package_object.id,
                        'license': license_object.id,
                    }
                    license_package_serializer = LicensePackageSerializer(data=license_package_data)
                    if license_package_serializer.is_valid(raise_exception=True):
                        license_package_serializer.save()
            except:
                return Response(license_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



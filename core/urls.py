from django.urls import path
from .api_views import Create, LicenseDetails
from django.contrib import admin

urlpatterns = [
    path("license", Create.as_view(), name="license_creation"),
    path("license/<slug:license_id>/", LicenseDetails.as_view(), name="License Details"),
]

admin.site.site_header = 'Licensing Administration Dashboard'
admin.site.index_title = 'Index'
admin.site.site_title = 'LaaS'
from django.urls import path
from .api_views import CreatePlan, FeatureList, CreateLicense, LicenseDetails, LicenseStatus, PlanDetails, FeatureDetails, PlanList
from django.contrib import admin


urlpatterns = [
    path('features/', FeatureList.as_view(), name="Feature List"),
    path('plans/', PlanList.as_view(), name="Plan List"),
    path("license", CreateLicense.as_view(), name="License Creation"),
    path("plan", CreatePlan.as_view(), name="License Creation"),
    path("license/status", LicenseStatus.as_view(), name="Update License Status"),
    path("license/<slug:license_id>/",
         LicenseDetails.as_view(), name="License Details"),
    path("plan/<slug:plan_id>/", PlanDetails.as_view(), name="Plan Details"),
    path("feature/<slug:feature_id>/",
         FeatureDetails.as_view(), name="Feature Details"),
]

admin.site.site_header = 'Licensing Administration Dashboard V5'
admin.site.index_title = 'Index'
admin.site.site_title = 'LaaS'

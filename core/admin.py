from django.contrib import admin
from .models import Feature, License, LicensePlan, Plan, FeaturePlan, LicenseFeature

# Register your models here.
admin.site.register(Feature)
admin.site.register(License)
admin.site.register(LicensePlan)
admin.site.register(Plan)
admin.site.register(FeaturePlan)
admin.site.register(LicenseFeature)

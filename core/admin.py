from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Feature, License, LicensePlan, Plan, FeaturePlan, LicenseFeature


class PlanInline(admin.TabularInline):
    model = LicensePlan
    extra = 0


class FeatureInline(admin.TabularInline):
    model = LicenseFeature
    extra = 0


class FeaturePlanInline(admin.TabularInline):
    model = FeaturePlan
    extra = 0


# Register your models here.
admin.site.register(Feature)
admin.site.register(Plan)
admin.site.register(FeaturePlan)
admin.site.register(License)
admin.site.register(LicensePlan)
admin.site.register(LicenseFeature)

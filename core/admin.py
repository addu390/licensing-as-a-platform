from gc import get_objects
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.db.models import *
from django.urls import reverse,resolve
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Feature, License, LicensePlan, Plan, FeaturePlan, LicenseFeature

class PlanInline(admin.TabularInline):
    model = LicensePlan
    extra = 0


class FeatureInline(admin.TabularInline):
    model = LicenseFeature
    extra = 0

# Register your models here.
admin.site.register(Feature)
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('display_plan', 'view_feature_link')

    def view_feature_link(self,obj):
        url = (
            reverse("admin:core_featureplan_changelist")
            + "?"
            + urlencode({"plan_id": f"{obj.external_id}"})
        )
        return format_html('<a href="{}">view</a>', url)
    view_feature_link.short_description = 'Linked feature'

@admin.register(FeaturePlan)
class FeaturePlanAdmin(admin.ModelAdmin):
    list_display = ('display_feature', 'display_plan')
    list_filter = ('plan_id',)

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license_id', 'view_plans_link', 'license_status')
    inlines = [PlanInline,FeatureInline]
    
    def view_plans_link(self,obj):
        count = obj.licenseplan_set.count()
        url = (
            reverse("admin:core_licenseplan_changelist")
            + "?"
            + urlencode({"license_id": f"{obj.license_id}"})
        )
        return format_html('<a href="{}">{} Plan(s)</a>', url, count)
    view_plans_link.short_description = 'Linked Plans'

@admin.register(LicensePlan)
class LicensePlanAdmin(admin.ModelAdmin):
    list_display = ('display_license', 'display_plan')
    list_filter = ('license_id',)

@admin.register(LicenseFeature)
class LicenseFeatureAdmin(admin.ModelAdmin):
    list_display = ('display_license','display_plan', 'display_feature')
    list_filter = ('license_id', 'feature_id')



from rest_framework import serializers

from core.models import License, LicensePlan, FeaturePlan, Plan, Feature


class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove', None)
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class LicenseSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = License
        fields = '__all__'


class PlanSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class FeatureSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class LicensePlanSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = LicensePlan
        fields = '__all__'


class FeaturePlanSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = FeaturePlan
        fields = '__all__'

from rest_framework import serializers

from core.models import License, LicensePackage, InclusionPackage, Package, Inclusion


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


class PackageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class InclusionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Inclusion
        fields = '__all__'


class LicensePackageSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = LicensePackage
        fields = '__all__'


class InclusionPackageSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = InclusionPackage
        fields = '__all__'

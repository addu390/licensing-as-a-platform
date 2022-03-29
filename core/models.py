from django.db import models
import uuid
from .constants import *
from licensing_platform.storage import PrivateMediaStorage


def new_uuid():
    key = uuid.uuid4()
    return str(key)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(
        max_length=255, unique=True, default=new_uuid)

    class Meta:
        abstract = True


class License(BaseModel):
    license_id = models.CharField(
        max_length=255, unique=True, default=new_uuid)
    linked_to = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(choices=LICENSE_STATUS,
                              default=ACTIVE, max_length=100)
    activation_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = LICENSE
        verbose_name_plural = LICENSE

    def __str__(self):
        return self.license_id


class Plan(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.FileField(blank=True, null=True,
                             storage=PrivateMediaStorage())
    type = models.CharField(choices=PLAN_TYPE, default=REGULAR, max_length=50)
    price = models.IntegerField(default=0)
    status = models.CharField(
        choices=BASE_STATUS, default=ACTIVE, max_length=100)

    class Meta:
        db_table = PLAN
        verbose_name_plural = PLAN

    def __str__(self):
        return self.name


class Feature(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.FileField(blank=True, null=True,
                             storage=PrivateMediaStorage())
    type = models.CharField(choices=FEATURE_TYPE, default=LIMIT, max_length=50)
    status = models.CharField(
        choices=BASE_STATUS, default=ACTIVE, max_length=100)

    class Meta:
        db_table = FEATURE
        verbose_name_plural = FEATURE

    def __str__(self):
        return self.name


class LicensePlan(BaseModel):
    license = models.ForeignKey(
        License, to_field='license_id', on_delete=models.DO_NOTHING)
    plan = models.ForeignKey(
        Plan, to_field='external_id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "license_plan"
        verbose_name_plural = "License and Plan"

    def __str__(self):
        return "%s -> %s" % (str(self.license), str(self.plan))


class FeaturePlan(BaseModel):
    feature = models.ForeignKey(Feature, to_field='external_id',
                                related_name="feature_plan", on_delete=models.DO_NOTHING)
    plan = models.ForeignKey(Plan, to_field='external_id',
                             related_name="selected_plan", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "feature_plan"
        verbose_name_plural = "Feature and Plan"

    def __str__(self):
        return "%s -> %s" % (str(self.plan), str(self.feature))


class LicenseFeature(BaseModel):
    license = models.ForeignKey(
        License, to_field='license_id', on_delete=models.DO_NOTHING)
    plan = models.ForeignKey(
        Plan, to_field='external_id', on_delete=models.DO_NOTHING)
    feature = models.ForeignKey(
        Feature, to_field='external_id', on_delete=models.DO_NOTHING)
    usage = models.IntegerField(default=0)
    threshold = models.IntegerField(default=0)

    class Meta:
        db_table = "license_feature"
        verbose_name_plural = "License and Feature"

    def __str__(self):
        return "%s -> %s -> %s" % (str(self.license), str(self.plan), str(self.feature))

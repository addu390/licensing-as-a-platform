from django.db import models
import uuid
from .constants import LICENSE_STATUS, BASE_STATUS


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(
        max_length=100,
        unique=True,
        default=str(uuid.uuid4()))

    class Meta:
        abstract = True


class License(BaseModel):
    license_key = models.CharField(max_length=255, unique=True, default=str(uuid.uuid4()))
    status = models.CharField(choices=LICENSE_STATUS, default="ACTIVE", max_length=100)
    activation_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "license"
        verbose_name_plural = "License"

    def __str__(self):
        return self.license_key


class Package(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    price = models.IntegerField(default=0)
    status = models.CharField(choices=BASE_STATUS, default="ACTIVE", max_length=100)
    type = models.BooleanField(default=True)

    class Meta:
        db_table = "package"
        verbose_name_plural = "package"

    def __str__(self):
        return self.title


class Inclusion(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    status = models.CharField(choices=BASE_STATUS, default="ACTIVE", max_length=100)
    type = models.BooleanField(default=True)

    class Meta:
        db_table = "inclusion"
        verbose_name_plural = "inclusion"

    def __str__(self):
        return self.title


class LicensePackage(BaseModel):
    license = models.ForeignKey(License, on_delete=models.DO_NOTHING)
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "license_package"
        verbose_name_plural = "License and Package"

    def __str__(self):
        return str(self.external_id)


class InclusionPackage(BaseModel):
    Inclusion = models.ForeignKey(License, related_name="inclusion_package", on_delete=models.DO_NOTHING)
    package = models.ForeignKey(Package, related_name="selected_package", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "inclusion_package"
        verbose_name_plural = "Inclusion and Package"

    def __str__(self):
        return str(self.external_id)

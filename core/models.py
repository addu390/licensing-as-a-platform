from django.db import models
import uuid

STATUS = (
    ("TRIAL", 'Trial License'),
    ("IN_PROGRESS", 'License activation in progress'),
    ("BLOCKED", 'License Blocked'),
    ("ACTIVE", 'License Active'),
    ("EXPIRED", 'License Validity Expired')
)

BUCKET_STATUS = (
    ("ACTIVE", "Active"),
    ("IN_ACTIVE", "In Active"),
)


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
    status = models.CharField(choices=STATUS, default="ACTIVE", max_length=100)
    activation_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "license"
        verbose_name_plural = "License"

    def __str__(self):
        return self.license_key


class Bucket(BaseModel):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True)
    price = models.IntegerField(default=0)
    status = models.CharField(choices=BUCKET_STATUS, default="ACTIVE", max_length=100)
    type = models.BooleanField(default=True)

    class Meta:
        db_table = "bucket"
        verbose_name_plural = "bucket"

    def __str__(self):
        return self.name

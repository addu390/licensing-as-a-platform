from django.urls import path
from .apiviews import Create

urlpatterns = [
    path("license", Create.as_view(), name="license_creation")
]
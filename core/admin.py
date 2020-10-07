from django.contrib import admin
from .models import Inclusion, License, LicensePackage, Package, InclusionPackage

# Register your models here.
admin.site.register(Inclusion)
admin.site.register(License)
admin.site.register(LicensePackage)
admin.site.register(Package)
admin.site.register(InclusionPackage)

from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Brands)
admin.site.register(models.Cars)
admin.site.register(models.Profile)
admin.site.register(models.Review)
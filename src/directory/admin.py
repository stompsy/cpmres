from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Agency)
admin.site.register(models.AgencyTag)
admin.site.register(models.AgencyType)
admin.site.register(models.Provider)
admin.site.register(models.ProviderTag)
admin.site.register(models.ProviderType)

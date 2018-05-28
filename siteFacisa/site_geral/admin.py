from django.contrib import admin
from site_geral.models import User, AccessRecord
from . import models
# Register your models here.

"""
Registro dos modelos na página do admin
"""
admin.site.register(User)
admin.site.register(AccessRecord)
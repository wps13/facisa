from django.contrib import admin
from site_geral.models import User, AccessRecord
# Register your models here.

admin.site.register(User)
admin.site.register(AccessRecord)
from django.contrib import admin
from django.contrib import auth
import django.contrib.auth.models

# Register your models here.
admin.site.unregister(auth.models.Group)
admin.site.unregister(auth.models.User)

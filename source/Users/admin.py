from django.contrib import admin

# Register your models here.

from Users.models import Profile

admin.site.register(Profile)
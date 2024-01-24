from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from shopA.models import Login
# Register your models here.

# admin.site.register(Login, UserAdmin)
from shopA.models import crud,image

admin.site.register(crud)
admin.site.register(image)
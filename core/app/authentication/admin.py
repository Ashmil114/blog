from django.contrib import admin
from .models import tb_user, CustomUser

admin.site.register(tb_user)
admin.site.register(CustomUser)

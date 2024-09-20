from django.contrib import admin
from .models import tb_post, tb_category


class post_admin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(tb_post, post_admin)
admin.site.register(tb_category)

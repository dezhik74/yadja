from django.contrib import admin

from yadja.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
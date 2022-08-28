from django.contrib import admin

from .models import Picture

class PictureAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Picture, PictureAdmin)
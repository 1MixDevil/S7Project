from django.contrib import admin
from .models import Yarik


class YarikAdmin(admin.ModelAdmin):
    list_display = ('aircraft_id', 'engine_position')
    list_display_links = ('aircraft_id', 'engine_position')


admin.site.register(Yarik, YarikAdmin)

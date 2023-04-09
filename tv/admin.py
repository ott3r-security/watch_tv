from django.contrib import admin
from .models import tvTime
from django.utils.encoding import smart_str



class tvTimeAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'days_on', 'length', 'provider')
    search_fields = ('show_name', 'provider', 'watcher')
    list_per_page = 100

admin.site.register(tvTime,tvTimeAdmin)
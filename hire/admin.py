from django.contrib import admin
from .models import PT
# Register your models here.


class PTAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'availability')
    search_fields = ['full_name', 'description']
    ordering = ('full_name',)
    prepopulated_fields = {'slug': ('full_name',)}


admin.site.register(PT, PTAdmin)

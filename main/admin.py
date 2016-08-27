from django.contrib import admin
from main.models import IK

# Register your models here.
class IKAdmin(admin.ModelAdmin):
    list_display = ('titre', 'numero', 'date')
    list_filter = ('date', 'numero')
    date_hierarchy = 'date'
    ordering = ('date', 'numero')
    search_fields = ('titre', 'texte', 'numero')

admin.site.register(IK, IKAdmin)

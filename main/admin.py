from django.contrib import admin
from main.models import IK, Article

# Register your models here.
class IKAdmin(admin.ModelAdmin):
    list_display = ('titre', 'numero', 'date')
    list_filter = ('date', 'numero')
    date_hierarchy = 'date'
    ordering = ('date', 'numero')
    search_fields = ('titre', 'texte', 'numero')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date')
    list_filter = ('date', 'auteur')
    date_hierarchy = 'date'
    ordering = ('date', 'auteur')
    search_fields = ('titre', 'texte', 'auteur')

admin.site.register(IK, IKAdmin)
admin.site.register(Article, ArticleAdmin)

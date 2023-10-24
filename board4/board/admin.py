from django.contrib import admin

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','created_at']
    list_display_links = ['title']


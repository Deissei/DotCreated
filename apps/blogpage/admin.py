from django.contrib import admin
from .models import Author, Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title', )}
    list_display = ['title']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Author)



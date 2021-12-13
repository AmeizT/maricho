from django.contrib import admin
from apps.posts.models import Post, Tech

class TechInline(admin.StackedInline):
    model = Tech

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'compensation']
    readonly_fields = ['created', 'updated']
    raw_id_fields = ['author']
    inlines = [
        TechInline
    ]

admin.site.register(Post, PostAdmin)

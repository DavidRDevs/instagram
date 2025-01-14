from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('user', 'caption', 'created_at')
    import_order = ('id',)
    export_order = ('id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'text', 'created_at')
    import_order = ('id',)
    export_order = ('id',)

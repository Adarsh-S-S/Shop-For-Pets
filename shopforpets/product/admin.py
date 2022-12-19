from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display= ('pro','name', 'cmt', 'date')

admin.site.register(Comment, CommentAdmin)
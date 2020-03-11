from django.contrib import admin
from .models import ArticleComment, Notification


@ admin.register (ArticleComment)
class CommentAdmin (admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'author', 'belong', 'create_date', 'show_content')
    list_filter = ('author', 'belong',)
    ordering = ('-id',)
    # Set the fields that need to be tagged with a
    list_display_links = ('id', 'show_content')

    # Use method to customize a field and set a name for this field
    def show_content (self, obj):
        return obj.content [: 30]

    show_content.short_description = 'Comment Content'


@ admin.register (Notification)
class NotificationAdmin (admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'create_p', 'create_date', 'comment', 'is_read')
    list_filter = ('create_p', 'is_read',)
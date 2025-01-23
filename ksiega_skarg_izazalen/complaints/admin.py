from django.contrib import admin
from .models import Topic, Comment

class CommentInline(admin.TabularInline):  # You can also use admin.StackedInline for a different layout
    model = Comment
    extra = 1  # Number of empty comment forms to display by default

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [CommentInline]  # Add the inline for comments

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'created_at')
    list_filter = ('topic',)
    search_fields = ('author', 'content')

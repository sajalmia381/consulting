from django.contrib import admin
from .models import Blog, Comment, Reply, Tag

# Register your models here.


admin.site.register(Tag)


class BlogCommentInline(admin.TabularInline):
    model = Comment
    max_num = 0


class BlogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    inlines = [BlogCommentInline]
    list_filter = ['timestrimp']

    class Meta:
        model = Blog


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'blog']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_filter = ['comment', 'timestrimp']
    list_display = ['email', 'timestrimp']

    class Meta:
        model = Reply


admin.site.register(Reply, ReplyAdmin)
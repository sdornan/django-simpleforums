from django.contrib import admin

from proto.forums.models import Forum, Thread, Post


class ForumAdmin(admin.ModelAdmin):
    pass


class PostInline(admin.TabularInline):
    model = Post
    fields = ['author', 'body', 'created']
    readonly_fields = ['created']


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'creator', 'created']
    list_filter = ['forum', 'creator']
    inlines = [PostInline]


admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)

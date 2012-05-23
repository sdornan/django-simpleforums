from django.conf.urls import patterns, url

from proto.forums.views import ForumListView, ThreadListView, PostListView


urlpatterns = patterns('proto.forums.views',
    url(r'^(?P<forum_slug>[-\w]+)/create-thread/$', 'create_thread', name='create-thread'),
    url(r'^(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/process-post/$', 'process_post_form', name='process-post'),
    url(r'^(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<forum_slug>[-\w]+)/$', ThreadListView.as_view(), name='thread-list'),
    url(r'^$', ForumListView.as_view(), name='forum-list'),
    url(r'^posts/(?P<post_id>\d+)/form/$', 'ajax_post_form', name='ajax-post-form'),
    url(r'^(?P<forum_slug>[-\w]+)/(?P<thread_slug>[-\w]+)/(?P<post_id>[-\w]+)/process-post/$',
        'process_post_form', name='process-post'),
)

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from proto.forums.forms import ThreadForm, PostInlineFormSet, PostForm
from proto.forums.models import Forum, Thread, Post

from pure_pagination.mixins import PaginationMixin


class ForumListView(ListView):
    """
    Displays a list of all the forums.
    """
    # Retrieves the number of threads and posts in each forum for display with the queryset
    queryset = Forum.on_site.all().annotate(num_threads=Count('thread', distinct=True),
                                            num_posts=Count('thread__post', distinct=True))


class ThreadListView(PaginationMixin, ListView):
    """
    Displays a list of the threads in a particular forum.
    """
    def get_queryset(self):
        self.forum = get_object_or_404(Forum, slug=self.kwargs['forum_slug'], site=settings.SITE_ID)
        return Thread.objects.filter(forum=self.forum).select_related('creator', 'forum').annotate(num_posts=Count('post'))

    def get_context_data(self, **kwargs):
        context = super(ThreadListView, self).get_context_data(**kwargs)
        context['forum'] = self.forum
        return context


class PostListView(PaginationMixin, ListView):
    """
    Displays a list of the posts in a particular thread.
    """
    paginate_by = 10

    def get_queryset(self):
        self.thread = get_object_or_404(Thread.objects.select_related('forum'),
                                        slug=self.kwargs['thread_slug'], forum__site=settings.SITE_ID)
        return Post.objects.filter(thread=self.thread).select_related('author', 'author__userprofile')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['thread'] = self.thread
        context['post_form'] = PostForm()
        return context


@login_required
def create_thread(request, forum_slug):
    """
    Builds and displays the form for a new thread, and processes that form.
    """
    forum = get_object_or_404(Forum, slug=forum_slug, site=settings.SITE_ID)

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            # Sets the forum and creator of the thread, which aren't part of the form
            form.instance.forum = forum
            form.instance.creator = request.user
            thread = form.save(commit=False)

            # Uses an inline formset in order to create the thread and its first post using the same form
            post_formset = PostInlineFormSet(request.POST, instance=thread)
            if post_formset.is_valid():
                for form in post_formset.forms:
                    # Sets the author of the post
                    form.instance.author = request.user
                thread.save()
                post_formset.save()

                messages.success(request, "Your thread <em>%s</em> was created." % thread.title)

            return redirect(thread.get_absolute_url())
    else:
        form = ThreadForm()
        post_formset = PostInlineFormSet(instance=Thread())

    return render(request, 'forums/thread_form.html', {
        'form': form,
        'post_formset': post_formset,
        'forum': forum
    })


@login_required
@require_POST
def process_post_form(request, forum_slug, thread_slug, post_id=None):
    """
    Processes a form for a post, both create and edit.
    """
    created = not post_id

    # Makes sure that the user is posting to an existing thread
    thread = get_object_or_404(Thread.objects.select_related('forum'),
                               slug=thread_slug, forum__slug=forum_slug, forum__site=settings.SITE_ID)

    if not created:
        # User is editing a post
        post = get_object_or_404(Post, pk=post_id)
        if post.author != request.user:
            raise HttpResponseForbidden()
    else:
        # User is creating a post
        post = Post(author=request.user, thread=thread)

    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()

        if created:
            # Saves the thread without any changes so that its modified field gets updated
            # and it gets moved to the top of its forum's thread list
            # Only do this if it's a new post, not an edit of an existing post
            thread.save()

        if not created:
            messages.success(request, "Your post was updated successfully.")
        else:
            messages.success(request, "Your post was successful.")

    return redirect(thread.get_absolute_url())


def ajax_post_form(request, post_id):
    """
    Builds a form for a post.
    """
    if not request.is_ajax():
        raise Http404

    post = get_object_or_404(Post.objects, pk=post_id)

    post_form = PostForm(instance=post)

    return render(request, 'forums/post_form.html', {
        'post_form': post_form,
        'post': post
    })

from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from forums.models import Thread, Post


class ThreadForm(ModelForm):

    class Meta:
        model = Thread
        exclude = ('forum', 'creator')


class PostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ('thread', 'author')


PostInlineFormSet = inlineformset_factory(Thread, Post, form=PostForm, can_delete=False, max_num=1)

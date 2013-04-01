from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from feeds.models import Feed, Tag, FeedType
from profiles.models import Student

class FeedListView(ListView):
    queryset = Feed.objects.all().order_by('-created_on')
    context_object_name = 'feeds'
    template_name = 'feed_list.html'

    def get_context_data(self, **kwargs):
        context = super(FeedListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedPopularListView(ListView):
    queryset = Feed.objects.all().order_by('-vote')
    context_object_name = 'feeds'
    template_name = 'feed_list.html'

    def get_context_data(self, **kwargs):
        context = super(FeedPopularListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedTypeListView(ListView):
    context_object_name = 'feeds'
    template_name = 'feed_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        feed_type = FeedType.objects.get(slug=slug)
        return Feed.objects.filter(feed_type=feed_type)

    def get_context_data(self, **kwargs):
        context = super(FeedTypeListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedTagListView(ListView):
    context_object_name = 'feeds'
    template_name = 'feed_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=slug)
        return tag.feed_set.all()

    def get_context_data(self, **kwargs):
        context = super(FeedTagListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class FeedDetailView(DetailView):
    model = Feed
    context_object_name = 'feed'
    template_name = 'feed_detail.html'


class FeedCreateView(LoginRequiredMixin, CreateView):
    model = Feed
    template_name = 'feed/feed_create.html'
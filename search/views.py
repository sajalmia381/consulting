from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from blog.models import Blog


def search_view(request):
    query = request.GET.get('q')
    if query.exists():
        obj = Blog.objects.search(query)
    return Blog.objects.all()


class SearchView(ListView):
    template_name = 'search/search_list.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return Blog.objects.search(query)
        return Blog.objects.all()
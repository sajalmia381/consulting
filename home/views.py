from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from category.models import Category
from blog.models import Blog
from service.models import Service, Feature
from contact.forms import QuoteForm
from about.models import Team, WhoWeAre
from .models import IndexBanner, Partner, Achievement, Testimonial
# Create your views here.


class IndexView(ListView):

    template_name = 'home/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banner'] = IndexBanner.objects.all()[:3]
        context['services'] = Service.objects.all()
        context['partners'] = Partner.objects.all()
        context['blogs'] = Blog.objects.all()[:3]
        context['achievements'] = Achievement.objects.all()
        context['categorys'] = Category.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['features'] = Feature.objects.all()[:3]
        context['quote'] = QuoteForm(self.request.POST or None)
        try:
            context['ceo'] = Team.objects.get(title__icontains='ceo', active=True)
        except Team.DoesNotExist:
            context['ceo'] = None

        context['whoweare'] = WhoWeAre.objects.first()

        return context
















        return context

    def get_queryset(self):
        qs_banner = IndexBanner.objects.all()
        return qs_banner

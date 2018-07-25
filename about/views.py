from django.shortcuts import render
from django.views.generic import ListView

from home.models import Partner, Achievement
from .models import Team, AboutUs, AboutCompany, Experience
# Create your views here.


class AboutView(ListView):

    template_name = 'about/about.html'
    queryset = 'object_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['partners'] = Partner.objects.all()
        context['achivements'] = Achievement.objects.all()[:4]
        context['aboutus'] = AboutUs.objects.first()
        context['about_company'] = AboutCompany.objects.all()[:3]
        context['experience'] = Experience.objects.first()
        return context

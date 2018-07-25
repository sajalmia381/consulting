from django.shortcuts import render, get_object_or_404
from django.views import generic

from home.models import Partner
from .models import Portfolio
from category.models import Category
# Create your views here.


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioView, self).get_context_data(*args, **kwargs)
        context['partners'] = Partner.objects.all()
        context['categorys'] = Category.objects.all()
        return context


class PortfolioDetails(generic.DetailView):
    model = Portfolio

    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioDetails, self).get_context_data(*args, **kwargs)
        context['partners'] = Partner.objects.all()
        return context

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Portfolio, pk=pk)
        return obj

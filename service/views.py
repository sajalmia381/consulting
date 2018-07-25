from django.shortcuts import render, get_object_or_404
from django.views import generic

from home.models import Partner
from .models import Service, PriceTable

# Create your views here.


class ServiceDetailsView(generic.DetailView):

    template_name = 'service/service_details.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailsView, self).get_context_data(**kwargs)
        context['service_list'] = Service.objects.all()
        context['partners'] = Partner.objects.all()
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        qs = get_object_or_404(Service, slug=slug)
        return qs


class ServiceListView(generic.ListView):

    model = Service
    template_name = 'service/service_list.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        context['price_table'] = PriceTable.objects.all()[:4]
        return context

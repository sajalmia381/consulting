from django.urls import path
from .views import ServiceListView, ServiceDetailsView

app_name = 'service'

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<slug>/', ServiceDetailsView.as_view(), name='service_details'),
]
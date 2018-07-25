from django.urls import path

from .views import PortfolioView, PortfolioDetails

app_name = 'portfolio'
urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio_list'),
    path('<pk>', PortfolioDetails.as_view(), name='portfolio_details'),
]
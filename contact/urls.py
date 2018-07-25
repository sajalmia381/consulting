from django.urls import path

from .views import ContactView, quote_submit, contact_form_view, quote_view

app_name = 'contact'
urlpatterns = [
    # path('', ContactView.as_view(), name='contact_index'),
    path('', contact_form_view, name='contact_index'),
    path('quote-submit', quote_submit, name='quote_submit'),
    path('quote', quote_view, name='quote'),
]
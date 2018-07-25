from django.contrib import admin
from .models import Portfolio
# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):

    model = Portfolio

    list_display = ['title', 'get_service']

    def get_service(self, obj):
        return obj.service.name

    get_service.admin_order_field = 'service'

    list_filter = ['service__name']


admin.site.register(Portfolio, PortfolioAdmin)

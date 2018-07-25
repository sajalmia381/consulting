from django.contrib import admin
from .models import Service, Feature, PriceTable, PriceTableFeature

# Register your models here.


admin.site.register(Service)

admin.site.register(Feature)


class PriceTableAdminInlines(admin.TabularInline):
    model = PriceTableFeature
    max_num = 0


class PriceTableAdmin(admin.ModelAdmin):
    inlines = [PriceTableAdminInlines]

    class Meta:
        model = PriceTable


admin.site.register(PriceTable)

admin.site.register(PriceTableFeature)

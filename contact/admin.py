from django.contrib import admin
from .models import FormContact, Quote


class FormContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestrimp']

    class Meta:
        model = FormContact


admin.site.register(FormContact, FormContactAdmin)

admin.site.register(Quote)





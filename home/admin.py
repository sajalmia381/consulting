from django.contrib import admin
from .models import IndexBanner, Partner, Achievement, Testimonial
# Register your models here.

admin.site.register(IndexBanner)

admin.site.register(Partner)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'total']

    class Meta:
        model = Achievement


admin.site.register(Achievement, AchievementAdmin)

admin.site.register(Testimonial)
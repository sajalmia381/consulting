from django.contrib import admin

from .models import Team, AboutUs, AboutCompany, GeneralInformation, MessageFromTeam, WhoWeAre, CompanyStrategy, Experience
# Register your models here.


admin.site.register(GeneralInformation)


class TeamAdminInline(admin.TabularInline):
    model = MessageFromTeam
    max_num = 1


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'active']
    inlines = [TeamAdminInline]

    class Meta:
        model = Team


admin.site.register(Team, TeamAdmin)

admin.site.register(AboutUs)

admin.site.register(AboutCompany)

admin.site.register(CompanyStrategy)

admin.site.register(Experience)

admin.site.register(WhoWeAre)

admin.site.register(MessageFromTeam)
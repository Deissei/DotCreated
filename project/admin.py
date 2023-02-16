from django.contrib import admin
from project.models import Services, Contact, Rewiews, Plan, Category
from apps.aboutpage.models import AboutModels

class SevricesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title', )}
    list_display = ['title']

class PlanAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title', )}
    list_display = ['title']


admin.site.register(Services, SevricesAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Category)
admin.site.register(Rewiews)
admin.site.register(Contact)
admin.site.register(AboutModels)
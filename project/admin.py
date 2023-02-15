from django.contrib import admin
from project.models import Services, Employee, Contact, Rewiews, Plan, Category

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
admin.site.register(Employee)
admin.site.register(Contact)
from django.shortcuts import render
from project.models import Services, Employee, Contact, Category, Rewiews, Plan


def homepage_index(request):
    services = Services.objects.all()
    plan = Plan.objects.all()
    category = Category.objects.all()
    rewiews = Rewiews.objects.all()
    employee = Employee.objects.all()
    contact = Contact.objects.all()
    context = {
        'services': services,
        'plan': plan,
        'category': category,
        'rewiews': rewiews,
        'employee': employee,
        'contact': contact,
    }
    return render(request, 'index.html', context)



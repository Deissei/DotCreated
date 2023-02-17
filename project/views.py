from django.shortcuts import render
from project.models import Services, Contact, Category, Rewiews, Plan
from apps.aboutpage.models import AboutModels
from apps.blogpage.models import Blog
from django.views.generic import View


def homepage_index(request):
    services = Services.objects.all()
    category = Category.objects.all()
    rewiews = Rewiews.objects.all()
    rewiews1 = Rewiews.objects.order_by('?')
    contact = Contact.objects.all()
    plan = Plan.objects.filter(id=1)
    plan2 = Plan.objects.filter(id=2)
    plan3 = Plan.objects.filter(id=4)
    plan4 = Plan.objects.filter(id=5)
    context = {
        'services': services,
        'category': category,
        'rewiews': rewiews,
        'rewiews1': rewiews1,
        'contact': contact,
        'plan': plan,
        'plan2': plan2,
        'plan3': plan3,
        'plan4': plan4,
    }
    return render(request, 'index.html', context)

def about(request):
    about = AboutModels.objects.filter(id=1)
    about2 = AboutModels.objects.filter(id=2)
    about3 = AboutModels.objects.filter(id=3)
    category = Category.objects.all()
    context = {
        'about': about,
        'about2': about2,
        'about3': about3,
        'category': category,
    }
    return render(request, 'about.html', context)

def services(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services1.html', context)

def work(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'gallery-regular.html', context)

def contact(request):
    contact = Contact.objects.all()
    context = {
        'contact': contact
    }
    return render(request, 'contact2.html', context)

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, 'blog-1.html', context)

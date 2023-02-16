from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from project.views import homepage_index, about, services, work, contact

urlpatterns = [
    path('', homepage_index, name='homepage'),
    path('services/', services, name='services'),
    path('work-gallery', work, name='work'),
    path('about/', about, name='aboutpage'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
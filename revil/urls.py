
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = {
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),
    path('', views.HOMEPAGE, name='homepage'),

    path('contact', views.CONTACT, name='contact'),
    path('about', views.ABOUT, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),


}

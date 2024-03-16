"""
URL configuration for imagefixer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home, upload_image
from .views import edit_image
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('upload_image/', upload_image, name='upload_image'),
    path('edit-image/', views.edit_image, name='edit_image'),
    path('edit_image/', edit_image, name='edit_image'),
    path('services/', views.services, name='services'),
]


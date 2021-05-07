"""kodedautos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cars import views as car_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include
from account import views as acc_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', car_view.CarsList.as_view(), name='home'),
    path('cars/<slug>/', car_view.CarDetail.as_view(), name='cardetail'),
    path('addcar/', car_view.CarCreate.as_view(), name='carcreate'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('cars/delete/<slug>/', car_view.DeleteCar.as_view(), name = 'deletecar'),
    path('cars/edit/<slug>/', car_view.UpdateCar.as_view(), name = 'updatecar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
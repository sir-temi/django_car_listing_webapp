from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('dashboard/', views.DashBaoard.as_view(), name='dashboard'),
]

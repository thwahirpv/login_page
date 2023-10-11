from django.urls import path
from . import views


urlpatterns = [
    path('', views.log_in, name='login'),
    path('homepage/', views.home, name='homepage'),
    path('logout',views.log_out, name='logout'),
    path('contact/', views.contact, name='contact')
]   
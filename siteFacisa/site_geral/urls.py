from django.urls import path
from site_geral import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('inicio/', views.inicio, name = 'inicio'),
    path('sobre/', views.sobre, name = 'sobre'), 
    path('acessos/', views.acessos, name='acessos'),
]
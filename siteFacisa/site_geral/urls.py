from django.urls import path
from site_geral import views

urlpatterns = 
"""
Urlspatters configura as urls que serão requisitas pelo usuário,
ao requisitar um caminho especifico, ocorrerá o redirecionamento 
para a view especificada
"""
[
    path('',views.inicio,name='inicio'),
    path('inicio/', views.inicio, name = 'inicio'),
    path('sobre/', views.sobre, name = 'sobre'), 
    path('acessos/', views.acessos, name='acessos'),
]
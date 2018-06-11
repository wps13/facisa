from django.urls import path
from site_geral import views

"""
Urlspatters configura as urls que serão requisitas pelo usuário,
ao requisitar um caminho especifico, ocorrerá o redirecionamento 
para a view especificada
"""
urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('inicio/', views.inicio, name = 'inicio'),
    path('sobre/', views.sobre, name = 'sobre'), 
    path('acessos/', views.acessos, name='acessos'),
    path('cargas/', views.controleCarga, name='cargas'),
]
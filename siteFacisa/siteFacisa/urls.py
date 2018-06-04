"""siteFacisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include

#from django.conf.urls import include
from django.conf import settings
from site_geral import views

""""
Inclue as urls configuradas no arquivo site_geral.urls através do include 
e define o caminho para a página do administrador ( admin)
"""
urlpatterns = [
    path('', include('site_geral.urls')),
    path('admin/', admin.site.urls),
]

"""
Caso o debug esteja ativado e esteja no ip especifica no arquivo settings.py,
é retornado a barra lateral em conjunto com as urls previamente configuradas
"""
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls) )
    ] + urlpatterns

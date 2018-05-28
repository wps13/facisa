from django.shortcuts import render
from site_geral.models import AccessRecord, User

"""
Retorna a página de inicio
"""
def inicio(request):
    return render(request, 'site_geral/inicio.html')

"""
Retorna a página com as informações sobre o projeto
"""
def sobre(request):
    return render(request, 'site_geral/about.html')

"""

"""
def acessos(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'site_geral/acessos.html',context= date_dict)
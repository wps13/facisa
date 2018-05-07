from django.shortcuts import render
from site_geral.models import AccessRecord, User

def inicio(request):
    return render(request, 'site_geral/inicio.html')

def cadastro(request):
    return render(request, 'site_geral/cadastro.html')

def sobre(request):
    return render(request, 'site_geral/about.html')

def acessos(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'site_geral/acessos.html',context= date_dict)
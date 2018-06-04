from django.shortcuts import render
from site_geral.models import AccessRecord, User


def inicio(request):
"""
Retorna a página de inicio
"""
    return render(request, 'site_geral/inicio.html')


def sobre(request):
"""
Retorna a página com as informações sobre o projeto
"""
    return render(request, 'site_geral/about.html')


def acessos(request):
"""
Função que recupera os acessos feitos ordenando pela data,
para depois exibi-los na página acessos.html
Como o contéudo é armazenado em um dicionário,tipo de estrutura
composto por pares chave e valor, que nesse caso seria o nome e data, respectivamente,
é possível percorre-lo e exibir tais dados, caso não estejam vazios
"""
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'site_geral/acessos.html',context= date_dict)
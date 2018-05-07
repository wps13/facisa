from django.shortcuts import render

def inicio(request):
    return render(request, 'site_geral/inicio.html')

def cadastro(request):
    return render(request, 'site_geral/cadastro.html')

def sobre(request):
    return render(request, 'site_geral/about.html')
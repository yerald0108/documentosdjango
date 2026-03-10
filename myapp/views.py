from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def formulario_f01(request):
    return render(request, 'myapp/F.01_documento.html')


def formulario_f07(request):
    return render(request, 'myapp/F.07_documento.html')


def formulario_f12(request):
    return render(request, 'myapp/F.12_documento.html')


def formulario_f42(request):
    return render(request, 'myapp/F.42documento.html')


def formulario_f60(request):
    return render(request, 'myapp/F.60_documento.html')
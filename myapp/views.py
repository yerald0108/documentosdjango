from django.shortcuts import render

# Create your views here.

def formulario_f12(request):
    return render(request, 'myapp/formulario_f12.html')
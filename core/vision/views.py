from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def datosActuales(request):
    return render(request, 'pages/datosactuales.html')

def ultimosDatos(request):
    return render(request, 'pages/ultimosdatos.html')
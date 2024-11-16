from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje="hola soy un mensaje"
    return render(request, 'mainapp/index.html',{
        'title': 'inicio',
        'content': 'Bienvenido a la pagina principal',
        'mensaje': mensaje
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title': 'Acerca de nosotros',
        'content': 'Somos un equipo de desarrollo de software'
    })

def mision(request):
    return render(request, 'mainapp/mision.html',{
        'title': 'Misión',
        'content': 'Mision de la empresa'
    })

def vision(request):
    return render(request, 'mainapp/vision.html',{
        'title': 'Visión',
        'content': 'Visión de la empresa'
    })
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html'),{
        'title':'Django | Inicio ',
        'content': 'inicio/',}

def acercade(request):
    return render(request, 'about.html'),{
        'title':'Django | About ',
        'content': 'about/',}

def index(request):
    return render(request, 'mision.html'),{
        'title':'Django | Mision ',
        'content': 'Mision/',}

def index(request):
    return render(request, 'vision.html'),{
        'title':'Django | Vision ',
        'content': 'vision/',}
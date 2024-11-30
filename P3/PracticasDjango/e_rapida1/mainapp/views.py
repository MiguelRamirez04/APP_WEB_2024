from django.shortcuts import render, redirect
#from django.shortcuts import redirect
#from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html'),{
        'title':'Django | Inicio ',
        'content': 'inicio/',}

def about(request):
    return render(request, 'about.html'),{
        'title':'Django | Acerca de ',
        'content': 'acerca de/',}

def mision(request):
    return render(request, 'mision.html'),{
        'title':'Django | Mision ',
        'content': 'mision/',}

def vision(request):
    return render(request, 'vision.html'),{
        'title':'Django | Vision ',
        'content': 'vision/',}

def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
        messages.success(request, "Ya estás autenticado")
    else:
#        register_form = UserCreationForm()
        register_form = RegisterForm()
        if request.method == "POST":
            register_form = RegisterForm(request.POST)
            #register_form = UserCreationForm(request.POST)

            if register_form.is_valid():
                register_form.save(commit=True)
                messages.success(request, "Registro exitoso")
                return redirect('inicio')


        return render(request, 'mainapp/registro.html', {
            'title':'Registros de usuario',
            'register_form':register_form
        })

def login_us(requets):
    return render(requets,'mainapp/login.html',{
        'title':'Inico de sesion',
        'content':'.::Formulario de Inicio de sesion::.'
    })
from django.shortcuts import render, redirect
#from django.shortcuts import redirect
#from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(requets):
    return render(requets,'mainapp/index.html',{
        'title':'inicio',
        'content':'.::bienvenido a mi pagina de inicio::.',
        'messages':'Esto es un mensaje'
    })

def about(requets):
    return render(requets,'mainapp/about.html',{
        'title':'acerca de',
        'content':'.::somos un equipo de SW multiplataforma con django::.'
    })

def mision(requets):
    return render(requets,'mainapp/mision.html',{
        'title':'mision',
        'content':'.::nuestra mision es crear aplicaciones web multiplataforma::.'
    })

def vision(requets):
    return render(requets,'mainapp/vision.html',{
        'title':'vision',
        'content':'.::nuestra vision es ser elmejor grupo de desarrollo de aplicaciones web'
    })

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


#redirigir error 404 primera forma
#def error404(request,exception):
#   return redirect('inicio')

#redirijir 2da forma

def error404_2(requets,exception):
    return render(requets,'mainapp/404.html')
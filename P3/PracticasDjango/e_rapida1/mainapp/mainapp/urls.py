from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from mainapp import views


urlpatterns = [
    path('',views.index,name='inicio'),
    path('inicio/',views.index,name='inicio'),
    path('acercade/',views.about,name='acercade'),
    path('mision/',views.mision,name='mision'),
    path('vision/',views.vision,name='vision'),
    path('registro/',views.registro,name='registro'),
    path('login/',views.login_us,name='login'),
    
]

#registro inicio de sesion
#formulario inicio de sesion
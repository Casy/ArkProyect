from django.shortcuts import render
from arkapp.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
#from forms import SignUpForm

def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))

def inicio_busqueda(request):
    return render_to_response('inicio-busqueda.html', context_instance=RequestContext(request))

def resultados_busqueda(request):
    return render_to_response('resultados-busqueda.html', context_instance=RequestContext(request))

def busqueda_avanzada(request):
    return render_to_response('busqueda-avanzada.html', context_instance=RequestContext(request))

def publicar_documento(request):
    return render_to_response('publicar-documento.html', context_instance=RequestContext(request))

def mis_referencias(request):
    return render_to_response('mis-referencias.html', context_instance=RequestContext(request))

def faq(request):
    return render_to_response('faq.html', context_instance=RequestContext(request))

def terminos_y_referencias(request):
    return render_to_response('terminos-y-referencias.html', context_instance=RequestContext(request))

def mis_valoraciones(request):
    return render_to_response('mis-valoraciones.html', context_instance=RequestContext(request))

def mis_publicaciones(request):
    return render_to_response('mis-publicaciones.html', context_instance=RequestContext(request))

def mis_referencias(request):
    return render_to_response('mis-referencias.html', context_instance=RequestContext(request))

def mi_perfil(request):
    return render_to_response('mi-perfil.html', context_instance=RequestContext(request))

def modificar_datos_usuario(request):
    return render_to_response('modificar-datos-usuario.html', context_instance=RequestContext(request))

def mis_estadisticas(request):
    return render_to_response('mis-estadisticas.html', context_instance=RequestContext(request))

def cerrar_sesion(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))

def consola_usuarios(request):
    return render_to_response('consola-usuarios.html', context_instance=RequestContext(request))




'''
def nuevousuario(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]	
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
			

            user.save()

            return HttpResponseRedirect('/privado')
			
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('nuevousuario.html', data, context_instance=RequestContext(request))
'''
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
	return render_to_response('ingresar.html', context_instance=RequestContext(request))

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
	
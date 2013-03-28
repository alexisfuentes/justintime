# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from principal.forms import loginForm

def view_index(request):
	if request.user.is_authenticated():
		return render_to_response('principal/index.html', context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')


def view_login(request):
	# Función para el logueo de los administradores
	msj = ""
	if request.POST:
		formulario = loginForm(request.POST)
		if formulario.is_valid():
			username = formulario.cleaned_data['username']
			password = formulario.cleaned_data['password']

			usuario = authenticate(username = username, password = password)

			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return HttpResponseRedirect('/')
			else:
				msj = "Contraseña o usuario no valido"
		ctx = {'mensaje' : msj}
		return render_to_response('principal/login.html', ctx, context_instance = RequestContext(request))
	else:
		return render_to_response('principal/login.html',{'mensaje':msj}, context_instance = RequestContext(request))
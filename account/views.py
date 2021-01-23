from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserEditForm

def index(request):
	return render(request, 'account/index.html')

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username = cd['username'], password = cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('user_profile')
				else:
					#######################################################
					# TODO : show message to user that user is disabled 1 #
					#######################################################
					return HttpResponse("user disabled")
			else:
				context = {
					'form': form
				}
				return render(request, 'account/login.html', context)
	else:
		form = LoginForm()
		context = {
			'form': form
		}
	return render(request, 'account/login.html', context)

def user_profile(request):
	context = {
		'user': request.user
	}
	return render(request, 'account/user-profile.html', context)

def user_edit(request):
	form = UserEditForm()
	context = {
		'form': form
	}
	return render(request, 'account/user-edit-profile.html', context)
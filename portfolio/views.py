# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse
from .forms import PortfolioForm, FeedbackForm
from .models import Portfolio
import datetime
from registration.backends.hmac.views import RegistrationView
from django.contrib import messages
from django.conf import settings

def Portfolio_detail(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = PortfolioForm(request.POST)
			if form.is_valid():
				detail = form.save(commit=False)
				detail.user = request.user
				detail.save()
				return redirect('Portfolio_display', username=detail.user, pk=detail.pk)
		else:	
			form = PortfolioForm
		return render(request, 'portfolio/details.html', {'form':form})
	else:
		return render(request,'portfolio/home.html',{})

def Portfolio_display(request, username, pk):
	detail = get_object_or_404(Portfolio, user__username=username, pk=pk)
	return render(request, 'portfolio/display.html', {'detail':detail})

def View_all(request):
	if request.user.is_authenticated():
		qs = Portfolio.objects.filter(user=request.user).order_by('pk')
		return render(request, 'portfolio/displayall.html', {"qs":qs})
	else:
		raise Http404

def home(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			detail = form.save(commit=False)
			detail.user = request.user
			detail.save()
			messages.success(request, 'Feedback submitted, you can submit another feedback.')
			form = FeedbackForm()
			return redirect('https://hoxnox.herokuapp.com/#feedback')
	else:	
		form = FeedbackForm
	return render(request, 'portfolio/home.html', {"form":form})

def editform(request, username, pk):
	instance = get_object_or_404(Portfolio, user__username=username, pk=pk)
	if request.user == instance.user:
		if request.method=="POST":
			form=PortfolioForm(request.POST, instance=instance)
			if form.is_valid():
				instance =  form.save(commit=False)
				instance.user = request.user
				instance.save()
				return redirect('Portfolio_display', username=instance.user, pk=instance.pk)
		else:
			form =  PortfolioForm(instance=instance)
		return render(request, 'portfolio/details.html',{'form':form})
	else:
		return render(request, 'portfolio/home.html',{})

def privacypolicy(request):
	return render(request, 'portfolio/privacypolicy.html', {})


def handler500(request):
    response = render(request, 'portfolio/500.html', {})
    response.status_code = 500
    return response
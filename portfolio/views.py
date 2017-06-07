# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PortfolioForm
from .models import Portfolio
import datetime
from registration.backends.hmac.views import RegistrationView

def Portfolio_detail(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			detail = Portfolio(request.user)
			form = PortfolioForm(request.POST)
			if form.is_valid():
				detail = form.save(commit=False)
				detail.save()
				return redirect('Portfolio_display', pk=detail.pk)
		else:	
			form = PortfolioForm
		return render(request, 'portfolio/details.html', {'form':form})
	else:
		return render(request,'portfolio/home.html',{})
def Portfolio_display(request, pk):
	if request.user.is_authenticated():
		detail = get_object_or_404(Portfolio, pk=pk)
		return render(request, 'portfolio/display.html', {'detail':detail})
	else:
		return render(request,'portfolio/home.html',{})		
def home(request):
	return render(request,'portfolio/home.html', {})	
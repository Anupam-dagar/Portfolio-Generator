from django import forms
from .models import Portfolio
class PortfolioForm(forms.ModelForm):
	main_bio = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Portfolio
		exclude = ['user']
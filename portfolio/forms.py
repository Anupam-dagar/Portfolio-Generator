from django import forms
from .models import Portfolio, Feedback
class PortfolioForm(forms.ModelForm):
	main_bio = forms.CharField(widget = forms.Textarea)
	widgets = {
		'date_of_birth': forms.DateInput(attrs={'id': 'id_date_of_birth'})
	}
	class Meta:
		model = Portfolio
		exclude = ['user']

class FeedbackForm(forms.ModelForm):
	feedback_field = forms.CharField(widget = forms.Textarea)

	class Meta:
		model = Feedback
		exclude = ['user']
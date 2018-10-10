"""User forms."""

# Django
from django import forms
from django.contrib.auth.models import User as UserAuth
from Users.models import User
from Users.models import Profile

class SignupForm(forms.Form):
	"""docstring for SignupForm"""
	username = forms.CharField(min_length=2, max_length=50)
	password = forms.CharField(max_length=70, widget=forms.PasswordInput())
	password_confirm = forms.CharField(max_length=70, widget=forms.PasswordInput())
	first_name = forms.CharField(min_length=2, max_length=50)
	last_name = forms.CharField(min_length=2, max_length=50)
	email = forms.CharField(min_length=6, max_length=40, widget=forms.EmailInput())

	def clean_username(self):
		"""pass"""
		username = self.cleaned_data['username']
		user_indb = User.objects.filter(username=username).exists()
		if user_indb:
			raise forms.ValidationError('El usuario ya está en uso')

		return username
		
	def clean(self):
		"""verify pass confirmation match"""
		data = super().clean()

		passwd = data['password']
		passwd_confirm = data['password_confirm']

		if passwd != passwd_confirm:
			raise forms.ValidationError('Las contraseñas no coinciden')

		return data

	def save(self):
		"""pass"""
		data = self.cleaned_data
		data.pop('password_confirm')
		user = User.objects.create_user(**data)
		profile = Profile(user=user)
		profile.save()
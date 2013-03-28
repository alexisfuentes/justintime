from django import forms

class loginForm(forms.Form):
	"""docstring for loginForm"""
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.PasswordInput(render_value = False))

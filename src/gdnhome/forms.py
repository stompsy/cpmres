from django import forms


class LoginForm(forms.Form):
    # username = forms.CharField(label="Email Address", max_length=100)
    email = forms.EmailField(label="Email Address", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

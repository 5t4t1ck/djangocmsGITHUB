from kine.models import KineProfile
from django.contrib.auth.models import User
from django import forms

class KineForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

class KineProfileForm(forms.ModelForm):
    class Meta:
        model = KineProfile
        fields = ('Establishment', 'Occupation')

class KineForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

from django import forms
from django.contrib.auth.models import User
from extra.models import Questionnaire , Messagerie , Contact
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ('q1','q21','q22','q23','q31','q32','q33')

class MessagerieForm(forms.ModelForm):
    class Meta:
        model = Messagerie
        fields = ['message','title']

class ContactForm(forms.ModelForm) :
    class Meta:
        model = Contact
        fields = ['userreceiver']


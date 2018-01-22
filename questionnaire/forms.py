from questionnaire.models import Questionnaire
from django import forms

class QuestionnaireForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super(QuestionnaireForm, self).__init__(*args, **kargs)

    class Meta:
         model = Questionnaire
         fields = '__all__'

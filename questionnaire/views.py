from django.shortcuts import render
from questionnaire.forms import QuestionnaireForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def choice(request):
    form = QuestionnaireForm()
    return render_to_response('questionnaire/choice.html',{'form': form})

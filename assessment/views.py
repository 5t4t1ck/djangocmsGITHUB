import json

from django.shortcuts import render
from extra.models import *
from django.contrib.auth.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

def assess_index(request):
    context = {
        'messages': Pessage.objects.all()
    }
    return render(request, 'assessment/index.html', context)

@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        msg_obj = json.loads(request.body.decode('utf-8'))
        try:
            u = User.objects.get(username="simon")
            v = UserProfile.objects.get(user = u)
            msg = Pessage.objects.create(user = v,user_names=msg_obj['user_name'], pessage=msg_obj['message'])
            msg.save()
        except:
            print("error saving message")
            return HttpResponse("error")
        return HttpResponse("success")

    else:
        return HttpResponseRedirect('/')

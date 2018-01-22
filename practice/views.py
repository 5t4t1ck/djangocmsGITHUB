from django.shortcuts import render
from extra.models import *
from django.contrib.auth.models import *
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from datetime import *
from extra.forms import UserForm, ContactForm, MessagerieForm


# Create your views here.

def kinect(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    user_autho = Authorization.objects.get(user=v)
    if request.method == 'POST':
        return HttpResponseRedirect('/practice/stage1/')
    return render_to_response(
            '../output/index.html',
            { 'user_autho' : user_autho }
            )
    

def menu(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    user_autho = Authorization.objects.get(user=v)
    template = loader.get_template('practice/menu.html')
    context = {
        'user_autho': user_autho,
    }
    return HttpResponse(template.render(context, request))

def messagerie(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    w = Messagerie.objects.filter(receiver = u.username)
    x = w.filter(read = False)
    y = x.count()
    template = loader.get_template('practice/messagerie.html')
    context = {
        'usermes': v,
        'read': y,
    }
    return HttpResponse(template.render(context, request))

def inbox(request):
    context = RequestContext(request)
    data = []
    data2 = []
    u = request.user
    v = UserProfile.objects.get(user = u)
    w = Messagerie.objects.filter(receiver = u.username)
    y = Messagerie.objects.filter(sender = u.username)
    for i in w :
        x = User.objects.get(username = i.sender)
        z1 = i.date
        z2 = x.first_name
        z3 = x.last_name
        z4 = i.title
        z5 = i.read
        z6 = i.id
        z7 = i.delrec
        data.append([z1,z2,z3,z4,z5,z6,z7])
    for j in y :
        k = User.objects.get(username = j.receiver)
        z11 = j.date
        z21 = k.first_name
        z31 = k.last_name
        z41 = j.title
        z51 = j.read
        z61 = j.id
        z71 = j.delsen
        data2.append([z11,z21,z31,z41,z51,z61,z71])
        
    data.reverse()
    data2.reverse()

    return render_to_response(
            'practice/inbox.html',
            {'data' : data, 'data2' : data2},
            context)

def read(request, pk):
    context = RequestContext(request)
    data = []
    c = []
    u = request.user
    v = UserProfile.objects.get(user = u)
    w = Messagerie.objects.get(pk = pk)
    x = User.objects.get(username = w.sender)
    y = User.objects.get(username = w.receiver)

    z1 = w.title
    z2 = w.date
    z3 = x.first_name
    z4 = x.last_name
    z5 = y.first_name
    z6 = y.last_name
    z7 = w.message

    data = [z1,z2,z3,z4,z5,z6,z7]

    
    if (u.username == y.username):
        w.read = True
    w.save()

    if (z1 == "[BOT] Questionnaire result") :
        a = UserProfile.objects.get(user = x)
        b = Questionnaire.objects.filter(user = a)
        c = b.latest('id')
    
    return render_to_response(
            'practice/read.html',
            {'data' : data, 'quest': c},
            context)

def write(request):
    context = RequestContext(request)
    data = []
    u = request.user
    v = UserProfile.objects.get(user = u)
    w = Contact.objects.filter(user = v)
    for i in w :
        x = User.objects.get(username = i.userreceiver)
        z1 = i.userreceiver
        z2 = x.first_name
        z3 = x.last_name
        data.append([z1,z2,z3])
        
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        message_form = MessagerieForm(data=request.POST)
        if user_form.is_valid() and message_form.is_valid() :
            profile = message_form.save(commit=False)
            profile.sender = u
            profile.receiver = request.POST['receiver']
            profile.save()
            return HttpResponseRedirect('/practice/messagerie/sent/')
        else:
            print(user_form.errors, message_form.errors)

    else:
        user_form = UserForm()
        message_form = MessagerieForm()

    return render_to_response(
            'practice/write.html',
            {'user_form': user_form, 'message_form': message_form, 'data' : data},
            context)


def contact(request):
    context = RequestContext(request)
    data = []
    u = request.user
    v = UserProfile.objects.get(user = u)
    w = Contact.objects.filter(user = v)
    for i in w :
        x = User.objects.get(username = i.userreceiver)
        z1 = i.userreceiver
        z2 = x.first_name
        z3 = x.last_name
        z4 = i.id
        data.append([z1,z2,z3,z4])
        
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        contact_form = ContactForm(data=request.POST)
        if user_form.is_valid() and contact_form.is_valid() :
            profile = contact_form.save(commit=False)
            profile.user = UserProfile.objects.get(user=request.user)
            profile.save()
            return HttpResponseRedirect('/practice/messagerie/contact/')
        else:
            print(user_form.errors, contact_form.errors)

    else:
        user_form = UserForm()
        contact_form = ContactForm()

    return render_to_response(
            'practice/contact.html',
            {'user_form': user_form, 'contact_form': contact_form, 'data' : data},
            context)

def delete(request, pk):
    context = RequestContext(request)
    w = Contact.objects.get(pk=pk)
    w.delete()
    return HttpResponseRedirect('/practice/messagerie/contact/')

def deletemesrec(request, pk):
    context = RequestContext(request)
    w = Messagerie.objects.get(pk=pk)
    w.delrec = True
    w.save()
    return HttpResponseRedirect('/practice/messagerie/inbox/')

def deletemessen(request, pk):
    context = RequestContext(request)
    w = Messagerie.objects.get(pk=pk)
    w.delsen = True
    w.save()
    return HttpResponseRedirect('/practice/messagerie/inbox/')

def sent(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    return render_to_response(
            'practice/sent.html',
            {'usermes': v},
            context)

def stage1(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    user_autho = Authorization.objects.get(user=v)
    stage = Stage1.objects.get(user=v)
    if stage.begin == date(2000, 1, 1) :
        stage.begin = date.today()
        stage.save()
    if stage.daystage1_set.count() == 0:
        stage.daystage1_set.create()
        day1 = DayStage1.objects.get(stage=stage)
        day1.day = 1
        day1.save()
    if stage.daystage1_set.count() != 0:
        day2 = DayStage1.objects.filter(stage=stage)
        day1 = day2.latest('id')
        if day1.date != date.today():
            stage.daystage1_set.create()
            y = day1
            day2 = DayStage1.objects.filter(stage=stage)
            day1 = day2.latest('id')
            day1.day = y.day + 1
            day1.save()
    template = loader.get_template('practice/stage1.html')
    context = {
        'user_autho': user_autho, 'stage': stage , 'day1': day1 
    }
    return HttpResponse(template.render(context, request))

def stage2(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    user_autho = Authorization.objects.get(user=v)
    stage = Stage2.objects.get(user=v)
    if stage.begin == date(2000, 1, 1) :
        stage.begin = date.today()
        stage.save()
    if stage.daystage2_set.count() == 0:
        stage.daystage2_set.create()
        day1 = DayStage2.objects.get(stage=stage)
        day1.day = 1
        day1.save()
    if stage.daystage2_set.count() != 0:
        day2 = DayStage2.objects.filter(stage=stage)
        day1 = day2.latest('id')
        if day1.date != date.today():
            stage.daystage2_set.create()
            y = day1
            day2 = DayStage2.objects.filter(stage=stage)
            day1 = day2.latest('id')
            day1.day = y.day + 1
            day1.save()
    template = loader.get_template('practice/stage2.html')
    context = {
        'user_autho': user_autho, 'stage': stage , 'day1': day1 
    }
    return HttpResponse(template.render(context, request))

def stage1education(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    template = loader.get_template('practice/stage1education.html')
    context = {
        'user_autho': user_autho, 'day1': day1 , 'stage' : stage
    }
    return HttpResponse(template.render(context, request))

def stage1cryo(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        day1.cryo = True
        day1.save()
        return HttpResponseRedirect('/practice/stage1/')
    return render_to_response(
            'practice/stage1cryo.html',
            { 'day1' : day1 , 'stage' : stage , 'user_autho' : user_autho },
            context)

def stage1ex(request):
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    template = loader.get_template('practice/stage1ex.html')
    context = {
        'user_autho': user_autho, 'day1': day1 , 'stage' : stage
    }
    return HttpResponse(template.render(context, request))

def stage1ex1set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex1set1t2 == True and day1.ex1set1t3 == False :
            day1.ex1set1t3 = True
            day1.save()
        if day1.ex1set1t1 == True and day1.ex1set1t2 == False :
            day1.ex1set1t2 = True
            day1.save()
        if day1.ex1set1t1 == False :
            day1.ex1set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex1set1/')    
    return render_to_response(
            'practice/stage1ex1set1.html',
            { 'day1' : day1, 'stage' : stage},
            context)

def stage1ex1set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex1set2t2 == True and day1.ex1set2t3 == False :
            day1.ex1set2t3 = True
            day1.save()
        if day1.ex1set2t1 == True and day1.ex1set2t2 == False :
            day1.ex1set2t2 = True
            day1.save()
        if day1.ex1set2t1 == False :
            day1.ex1set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex1set2/')
    return render_to_response(
            'practice/stage1ex1set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex1set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex1set3t2 == True and day1.ex1set3t3 == False :
            day1.ex1set3t3 = True
            day1.save()
        if day1.ex1set3t1 == True and day1.ex1set3t2 == False :
            day1.ex1set3t2 = True
            day1.save()
        if day1.ex1set3t1 == False :
            day1.ex1set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex1set3/')
    return render_to_response(
            'practice/stage1ex1set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)


def stage1ex2set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex2set1t2 == True and day1.ex2set1t3 == False :
            day1.ex2set1t3 = True
            day1.save()
        if day1.ex2set1t1 == True and day1.ex2set1t2 == False :
            day1.ex2set1t2 = True
            day1.save()
        if day1.ex2set1t1 == False :
            day1.ex2set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex2set1/')
    return render_to_response(
            'practice/stage1ex2set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex2set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex2set2t2 == True and day1.ex2set2t3 == False :
            day1.ex2set2t3 = True
            day1.save()
        if day1.ex2set2t1 == True and day1.ex2set2t2 == False :
            day1.ex2set2t2 = True
            day1.save()
        if day1.ex2set2t1 == False :
            day1.ex2set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex2set2/')
    return render_to_response(
            'practice/stage1ex2set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex2set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex2set3t2 == True and day1.ex2set3t3 == False :
            day1.ex2set3t3 = True
            day1.save()
        if day1.ex2set3t1 == True and day1.ex2set3t2 == False :
            day1.ex2set3t2 = True
            day1.save()
        if day1.ex2set3t1 == False :
            day1.ex2set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex2set3/')
    return render_to_response(
            'practice/stage1ex2set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)


def stage1ex3set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex3set1t2 == True and day1.ex3set1t3 == False :
            day1.ex3set1t3 = True
            day1.save()
        if day1.ex3set1t1 == True and day1.ex3set1t2 == False :
            day1.ex3set1t2 = True
            day1.save()
        if day1.ex3set1t1 == False :
            day1.ex3set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex3set1/')
    return render_to_response(
            'practice/stage1ex3set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex3set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex3set2t2 == True and day1.ex3set2t3 == False :
            day1.ex3set2t3 = True
            day1.save()
        if day1.ex3set2t1 == True and day1.ex3set2t2 == False :
            day1.ex3set2t2 = True
            day1.save()
        if day1.ex3set2t1 == False :
            day1.ex3set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex3set2/')
    return render_to_response(
            'practice/stage1ex3set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex3set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex3set3t2 == True and day1.ex3set3t3 == False :
            day1.ex3set3t3 = True
            day1.save()
        if day1.ex3set3t1 == True and day1.ex3set3t2 == False :
            day1.ex3set3t2 = True
            day1.save()
        if day1.ex3set3t1 == False :
            day1.ex3set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex3set3/')
    return render_to_response(
            'practice/stage1ex3set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)


def stage1ex4set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex4set1t2 == True and day1.ex4set1t3 == False :
            day1.ex4set1t3 = True
            day1.save()
        if day1.ex4set1t1 == True and day1.ex4set1t2 == False :
            day1.ex4set1t2 = True
            day1.save()
        if day1.ex4set1t1 == False :
            day1.ex4set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex4set1/')
    return render_to_response(
            'practice/stage1ex4set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex4set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex4set2t2 == True and day1.ex4set2t3 == False :
            day1.ex4set2t3 = True
            day1.save()
        if day1.ex4set2t1 == True and day1.ex4set2t2 == False :
            day1.ex4set2t2 = True
            day1.save()
        if day1.ex4set2t1 == False :
            day1.ex4set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex4set2/')
    return render_to_response(
            'practice/stage1ex4set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex4set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex4set3t2 == True and day1.ex4set3t3 == False :
            day1.ex4set3t3 = True
            day1.save()
        if day1.ex4set3t1 == True and day1.ex4set3t2 == False :
            day1.ex4set3t2 = True
            day1.save()
        if day1.ex4set3t1 == False :
            day1.ex4set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex4set3/')
    return render_to_response(
            'practice/stage1ex4set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)


def stage1ex5set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex5set1t2 == True and day1.ex5set1t3 == False :
            day1.ex5set1t3 = True
            day1.save()
        if day1.ex5set1t1 == True and day1.ex5set1t2 == False :
            day1.ex5set1t2 = True
            day1.save()
        if day1.ex5set1t1 == False :
            day1.ex5set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex5set1/')
    return render_to_response(
            'practice/stage1ex5set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex5set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex5set2t2 == True and day1.ex5set2t3 == False :
            day1.ex5set2t3 = True
            day1.save()
        if day1.ex5set2t1 == True and day1.ex5set2t2 == False :
            day1.ex5set2t2 = True
            day1.save()
        if day1.ex5set2t1 == False :
            day1.ex5set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex5set2/')
    return render_to_response(
            'practice/stage1ex5set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex5set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex5set3t2 == True and day1.ex5set3t3 == False :
            day1.ex5set3t3 = True
            day1.save()
        if day1.ex5set3t1 == True and day1.ex5set3t2 == False :
            day1.ex5set3t2 = True
            day1.save()
        if day1.ex5set3t1 == False :
            day1.ex5set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex5set3/')
    return render_to_response(
            'practice/stage1ex5set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex6set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex6set1t2 == True and day1.ex6set1t3 == False :
            day1.ex6set1t3 = True
            day1.save()
        if day1.ex6set1t1 == True and day1.ex6set1t2 == False :
            day1.ex6set1t2 = True
            day1.save()
        if day1.ex6set1t1 == False :
            day1.ex6set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex6set1/')
    return render_to_response(
            'practice/stage1ex6set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex6set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex6set2t2 == True and day1.ex6set2t3 == False :
            day1.ex6set2t3 = True
            day1.save()
        if day1.ex6set2t1 == True and day1.ex6set2t2 == False :
            day1.ex6set2t2 = True
            day1.save()
        if day1.ex6set2t1 == False :
            day1.ex6set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex6set2/')
    return render_to_response(
            'practice/stage1ex6set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex6set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex6set3t2 == True and day1.ex6set3t3 == False :
            day1.ex6set3t3 = True
            day1.save()
        if day1.ex6set3t1 == True and day1.ex6set3t2 == False :
            day1.ex6set3t2 = True
            day1.save()
        if day1.ex6set3t1 == False :
            day1.ex6set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex6set3/')
    return render_to_response(
            'practice/stage1ex6set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex7set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex7set1t2 == True and day1.ex7set1t3 == False :
            day1.ex7set1t3 = True
            day1.save()
        if day1.ex7set1t1 == True and day1.ex7set1t2 == False :
            day1.ex7set1t2 = True
            day1.save()
        if day1.ex7set1t1 == False :
            day1.ex7set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex7set1/')
    return render_to_response(
            'practice/stage1ex7set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex7set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex7set2t2 == True and day1.ex7set2t3 == False :
            day1.ex7set2t3 = True
            day1.save()
        if day1.ex7set2t1 == True and day1.ex7set2t2 == False :
            day1.ex7set2t2 = True
            day1.save()
        if day1.ex7set2t1 == False :
            day1.ex7set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex7set2/')
    return render_to_response(
            'practice/stage1ex7set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex7set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex7set3t2 == True and day1.ex7set3t3 == False :
            day1.ex7set3t3 = True
            day1.save()
        if day1.ex7set3t1 == True and day1.ex7set3t2 == False :
            day1.ex7set3t2 = True
            day1.save()
        if day1.ex7set3t1 == False :
            day1.ex7set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex7set3/')
    return render_to_response(
            'practice/stage1ex7set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex8set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex8set1t2 == True and day1.ex8set1t3 == False :
            day1.ex8set1t3 = True
            day1.save()
        if day1.ex8set1t1 == True and day1.ex8set1t2 == False :
            day1.ex8set1t2 = True
            day1.save()
        if day1.ex8set1t1 == False :
            day1.ex8set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex8set1/')
    return render_to_response(
            'practice/stage1ex8set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex8set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex8set2t2 == True and day1.ex8set2t3 == False :
            day1.ex8set2t3 = True
            day1.save()
        if day1.ex8set2t1 == True and day1.ex8set2t2 == False :
            day1.ex8set2t2 = True
            day1.save()
        if day1.ex8set2t1 == False :
            day1.ex8set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex8set2/')
    return render_to_response(
            'practice/stage1ex8set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex8set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex8set3t2 == True and day1.ex8set3t3 == False :
            day1.ex8set3t3 = True
            day1.save()
        if day1.ex8set3t1 == True and day1.ex8set3t2 == False :
            day1.ex8set3t2 = True
            day1.save()
        if day1.ex8set3t1 == False :
            day1.ex8set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex8set3/')
    return render_to_response(
            'practice/stage1ex8set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)


def stage1ex9set1(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex9set1t2 == True and day1.ex9set1t3 == False :
            day1.ex9set1t3 = True
            day1.save()
        if day1.ex9set1t1 == True and day1.ex9set1t2 == False :
            day1.ex9set1t2 = True
            day1.save()
        if day1.ex9set1t1 == False :
            day1.ex9set1t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex9set1/')
    return render_to_response(
            'practice/stage1ex9set1.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex9set2(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex9set2t2 == True and day1.ex9set2t3 == False :
            day1.ex9set2t3 = True
            day1.save()
        if day1.ex9set2t1 == True and day1.ex9set2t2 == False :
            day1.ex9set2t2 = True
            day1.save()
        if day1.ex9set2t1 == False :
            day1.ex9set2t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex9set2/')
    return render_to_response(
            'practice/stage1ex9set2.html',
            { 'day1' : day1, 'stage' : stage },
            context)

def stage1ex9set3(request):
    context = RequestContext(request)
    u = request.user
    v = UserProfile.objects.get(user=u)
    stage = Stage1.objects.get(user=v)
    day2 = DayStage1.objects.filter(stage=stage)
    day1 = day2.latest('id')
    user_autho = Authorization.objects.get(user=v)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        if day1.ex9set3t2 == True and day1.ex9set3t3 == False :
            day1.ex9set3t3 = True
            day1.save()
        if day1.ex9set3t1 == True and day1.ex9set3t2 == False :
            day1.ex9set3t2 = True
            day1.save()
        if day1.ex9set3t1 == False :
            day1.ex9set3t1 = True
            day1.save()
        return HttpResponseRedirect('/practice/stage1/exercise/ex9set3/')
    return render_to_response(
            'practice/stage1ex9set3.html',
            { 'day1' : day1, 'stage' : stage },
            context)


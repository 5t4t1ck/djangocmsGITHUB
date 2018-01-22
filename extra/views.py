from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from .models import *
from .forms import UserForm, QuestionnaireForm
from kine.models import KineProfile
from kine.forms import KineForm2
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
@login_required() # only logged in users should access this
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    pat = UserProfile.objects.get(user = user)
    try :
        s = pat.photo.url
        s = s[10:]
    except :
        s = ""
    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)
 
    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('photo','bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated() and (request.user.id == user.id or request.user.is_superuser == True) :
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                #if formset.is_valid():
                created_user.save()
                formset.save()
                if request.user.is_superuser == False :
                    return HttpResponseRedirect('/extra/profile/'+ str(pk)+'/')
                else :
                    return HttpResponseRedirect('/extra/profile/'+ str(pk)+'/')
 
        return render(request, "extra/update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
            "pat" : pat,
            "s" : s,
        })
    else:
        raise PermissionDenied

def profile_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    patient = UserProfile.objects.get(user = user)
    try :
        s = patient.photo.url
        s = s[10:]
    except :
        s = ""
    if request.user.is_authenticated() and (request.user.id == user.id or request.user.is_superuser == True) :

        return render(request, "extra/profile.html", {
            "patient" : patient,
            "s" : s,
        })
    else:
        raise PermissionDenied

def profile_kine(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    kine = KineProfile.objects.get(user = user)
    try :
        s = kine.photos.url
        s = s[10:]
    except :
        s = ""
    if request.user.is_authenticated() and (request.user.id == user.id or request.user.is_superuser == True) :

        return render(request, "extra/profilekine.html", {
            "kine" : kine,
            "s" : s,
        })
    else:
        raise PermissionDenied

def edit_kine(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    kine = KineProfile.objects.get(user = user)
    try :
        s = kine.photos.url
        s = s[10:]
    except :
        s = ""

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = KineForm2(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, KineProfile, fields=('Establishment', 'Occupation','photos'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id :
        if request.method == "POST":
            user_form = KineForm2(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    if request.user.is_superuser == False :
                        return HttpResponseRedirect('/extra/profilekine/'+ str(pk)+'/')
                    else :
                        return HttpResponseRedirect('/extra/profilekine/'+ str(pk)+'/')

        return render(request, "extra/updatekine.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
            "kine": kine,
            "s": s,
        })
    else:
        raise PermissionDenied

def questionnaire(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        question_form = QuestionnaireForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and question_form.is_valid() :
            profile = question_form.save(commit=False)
            profile.user = UserProfile.objects.get(user=request.user)
            profile.save()
            #assessment
            i = False
            if profile.q1 >= 9 :
                i = True
            if profile.q1 <9 :
                if profile.q22 == True :
                    i = True
                else :
                    i = False
            j = False
            if profile.q21 == True :
                j = True
            k = False
            if profile.q31 == True :
                k = True
 
            if (i == False and j == False and k == False) :
                return HttpResponseRedirect('/patient/practice/ok/')
            else :

                u = request.user
                v = UserProfile.objects.get(user = u)
                w = KineToUser.objects.get(user = v)
                x = w.kine
                y = User.objects.get(pk = x)
                msg = Messagerie.objects.create(message = " [Automatic message] I can't practice today, see my last questionnaire for more details.", title = "[BOT] Questionnaire result",sender = request.user.username,receiver = y.username) 
                msg.delsen = True
                msg.save()
                return HttpResponseRedirect('/patient/practice/denied/')

        else:
            print(user_form.errors, question_form.errors)

    else:
        user_form = UserForm()
        question_form = QuestionnaireForm()

    return render_to_response(
            'extra/questionnaire.html',
            {'user_form': user_form, 'question_form': question_form},
            context)

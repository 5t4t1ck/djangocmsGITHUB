from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

# Create your views here.

from kine.forms import KineForm, KineProfileForm
from kine.models import *
from extra.models import *
from extra.forms import *

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = KineForm(data=request.POST)
        profile_form = KineProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.is_superuser = True
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = KineForm()
        profile_form = KineProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'kine/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def registerpatient(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = KineForm(data=request.POST)
        profile_form = KineProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            user.is_superuser = False
            v = UserProfile.objects.get(user=user)
            v.kinetouser_set.create(kine = request.user.id)
            v.save()
            user.save()
            v = UserProfile.objects.get(user=user)
            v.authorization_set.create()
            v.stage1_set.create()
            v.stage2_set.create()
            w = Authorization.objects.get(user = v)
            w.stage1 = True
            w.stage2 = True
            w.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = KineForm()
        profile_form = KineProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'kine/registerpatient.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def patient(request):
    patient_list = KineToUser.objects.filter(kine = request.user.id)
    template = loader.get_template('kine/patient.html')
    context = {
        'patient_list': patient_list,
    }
    return HttpResponse(template.render(context, request))

def patientid(request):
    patient = KineToUser.objects.latest('id')
    template = loader.get_template('kine/patientid.html')
    context = {
        'patient': patient,
    }
    return HttpResponse(template.render(context, request))

def see(request, pk):
    context = RequestContext(request)
    patient = User.objects.get(pk = pk)
    
    return render_to_response(
            'kine/see.html',
            {'patient' : patient},
            context)

def questionnaire(request, pk):
    context = RequestContext(request)
    u = User.objects.get(pk=pk)
    v = UserProfile.objects.get(user=u)
    w = Questionnaire.objects.filter(user = v)
    data = []
    data1 = []
    data2 = []
    try :
        for i in w:
            data.append(i)
        data.reverse()
        data1 = data[0]
        del data[0]
        data2 = data
    except :
        data = []
    return render_to_response(
            'kine/questionnaire.html',
            {'data1' : data1, 'data2' : data2, 'patient' : u },
            context)

def questionnaireread(request, pk):
    context = RequestContext(request)
    w = Questionnaire.objects.get(pk=pk)
    return render_to_response(
            'kine/questionnaireread.html',
            {'quest' : w},
            context)

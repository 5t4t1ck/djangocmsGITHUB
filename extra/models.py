from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from kine.models import KineProfile
from patient.settings import *

scale = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    )
bool = (
    (True, 'True'),
    (False, 'False'),
    )
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    photo = models.ImageField(verbose_name=("Profile Picture"),
                      upload_to="/djangocms/media/", null=True, blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)

class KineToUser(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    kine = models.CharField(max_length=10, default='', blank=True)    

class Questionnaire(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    q1 = models.IntegerField(blank=True, default=0,choices=scale ,verbose_name="q1")
    q21 = models.BooleanField(blank=True, default=False,choices=bool ,verbose_name="q21")
    q22 = models.BooleanField(blank=True, default=False,choices=bool ,verbose_name="q22")
    q23 = models.BooleanField(blank=True, default=False,choices=bool ,verbose_name="q23")
    q31 = models.BooleanField(blank=True, default=False,choices=bool ,verbose_name="q31")
    q32 = models.BooleanField(blank=True, default=False,choices=bool ,verbose_name="q32")
    q33 = models.BooleanField(blank=True, default=False,choices=bool ,verbose_name="q33")
    creation = models.DateTimeField(auto_now=True)

class Authorization(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stage1 = models.BooleanField(blank = True, default = False)
    stage2 = models.BooleanField(blank = True, default = False)
    stage3 = models.BooleanField(blank = True, default = False)

class Stage1(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    begin = models.DateField(default = '2000-01-01')

class Stage2(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    begin = models.DateField(default = '2000-01-01')

class DayStage1 (models.Model):
    stage = models.ForeignKey(Stage1, on_delete=models.CASCADE)
    date = models.DateField(auto_now = True)
    day = models.IntegerField(blank=True, default=0)
    ex1set1t1 = models.BooleanField(blank=True, default=False)
    ex1set1t2 = models.BooleanField(blank=True, default=False)
    ex1set1t3 = models.BooleanField(blank=True, default=False)
    ex1set2t1 = models.BooleanField(blank=True, default=False)
    ex1set2t2 = models.BooleanField(blank=True, default=False)
    ex1set2t3 = models.BooleanField(blank=True, default=False)
    ex1set3t1 = models.BooleanField(blank=True, default=False)
    ex1set3t2 = models.BooleanField(blank=True, default=False)
    ex1set3t3 = models.BooleanField(blank=True, default=False)
    ex2set1t1 = models.BooleanField(blank=True, default=False)
    ex2set1t2 = models.BooleanField(blank=True, default=False)
    ex2set1t3 = models.BooleanField(blank=True, default=False)
    ex2set2t1 = models.BooleanField(blank=True, default=False)
    ex2set2t2 = models.BooleanField(blank=True, default=False)
    ex2set2t3 = models.BooleanField(blank=True, default=False)
    ex2set3t1 = models.BooleanField(blank=True, default=False)
    ex2set3t2 = models.BooleanField(blank=True, default=False)
    ex2set3t3 = models.BooleanField(blank=True, default=False)
    ex3set1t1 = models.BooleanField(blank=True, default=False)
    ex3set1t2 = models.BooleanField(blank=True, default=False)
    ex3set1t3 = models.BooleanField(blank=True, default=False)
    ex3set2t1 = models.BooleanField(blank=True, default=False)
    ex3set2t2 = models.BooleanField(blank=True, default=False)
    ex3set2t3 = models.BooleanField(blank=True, default=False)
    ex3set3t1 = models.BooleanField(blank=True, default=False)
    ex3set3t2 = models.BooleanField(blank=True, default=False)
    ex3set3t3 = models.BooleanField(blank=True, default=False)
    ex4set1t1 = models.BooleanField(blank=True, default=False)
    ex4set1t2 = models.BooleanField(blank=True, default=False)
    ex4set1t3 = models.BooleanField(blank=True, default=False)
    ex4set2t1 = models.BooleanField(blank=True, default=False)
    ex4set2t2 = models.BooleanField(blank=True, default=False)
    ex4set2t3 = models.BooleanField(blank=True, default=False)
    ex4set3t1 = models.BooleanField(blank=True, default=False)
    ex4set3t2 = models.BooleanField(blank=True, default=False)
    ex4set3t3 = models.BooleanField(blank=True, default=False)
    ex5set1t1 = models.BooleanField(blank=True, default=False)
    ex5set1t2 = models.BooleanField(blank=True, default=False)
    ex5set1t3 = models.BooleanField(blank=True, default=False)
    ex5set2t1 = models.BooleanField(blank=True, default=False)
    ex5set2t2 = models.BooleanField(blank=True, default=False)
    ex5set2t3 = models.BooleanField(blank=True, default=False)
    ex5set3t1 = models.BooleanField(blank=True, default=False)
    ex5set3t2 = models.BooleanField(blank=True, default=False)
    ex5set3t3 = models.BooleanField(blank=True, default=False)
    ex6set1t1 = models.BooleanField(blank=True, default=False)
    ex6set1t2 = models.BooleanField(blank=True, default=False)
    ex6set1t3 = models.BooleanField(blank=True, default=False)
    ex6set2t1 = models.BooleanField(blank=True, default=False)
    ex6set2t2 = models.BooleanField(blank=True, default=False)
    ex6set2t3 = models.BooleanField(blank=True, default=False)
    ex6set3t1 = models.BooleanField(blank=True, default=False)
    ex6set3t2 = models.BooleanField(blank=True, default=False)
    ex6set3t3 = models.BooleanField(blank=True, default=False)
    ex7set1t1 = models.BooleanField(blank=True, default=False)
    ex7set1t2 = models.BooleanField(blank=True, default=False)
    ex7set1t3 = models.BooleanField(blank=True, default=False)
    ex7set2t1 = models.BooleanField(blank=True, default=False)
    ex7set2t2 = models.BooleanField(blank=True, default=False)
    ex7set2t3 = models.BooleanField(blank=True, default=False)
    ex7set3t1 = models.BooleanField(blank=True, default=False)
    ex7set3t2 = models.BooleanField(blank=True, default=False)
    ex7set3t3 = models.BooleanField(blank=True, default=False)
    ex8set1t1 = models.BooleanField(blank=True, default=False)
    ex8set1t2 = models.BooleanField(blank=True, default=False)
    ex8set1t3 = models.BooleanField(blank=True, default=False)
    ex8set2t1 = models.BooleanField(blank=True, default=False)
    ex8set2t2 = models.BooleanField(blank=True, default=False)
    ex8set2t3 = models.BooleanField(blank=True, default=False)
    ex8set3t1 = models.BooleanField(blank=True, default=False)
    ex8set3t2 = models.BooleanField(blank=True, default=False)
    ex8set3t3 = models.BooleanField(blank=True, default=False)
    ex9set1t1 = models.BooleanField(blank=True, default=False)
    ex9set1t2 = models.BooleanField(blank=True, default=False)
    ex9set1t3 = models.BooleanField(blank=True, default=False)
    ex9set2t1 = models.BooleanField(blank=True, default=False)
    ex9set2t2 = models.BooleanField(blank=True, default=False)
    ex9set2t3 = models.BooleanField(blank=True, default=False)
    ex9set3t1 = models.BooleanField(blank=True, default=False)
    ex9set3t2 = models.BooleanField(blank=True, default=False)
    ex9set3t3 = models.BooleanField(blank=True, default=False)
    cryo = models.BooleanField(blank=True, default=False)

class DayStage2 (models.Model):
    stage = models.ForeignKey(Stage2, on_delete=models.CASCADE)
    date = models.DateField(auto_now = True)
    day = models.IntegerField(blank=True, default=0)

class Pessage(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_names = models.CharField(max_length=20)
    pessage = models.CharField(max_length=140)

class Messagerie(models.Model):
    message = models.TextField(default='', blank=True)
    title = models.CharField(max_length=200, blank=True, default='')
    sender = models.CharField(max_length=20, blank=True, default='')
    receiver = models.CharField(max_length=20, blank=True, default='')
    read = models.BooleanField(blank=True, default=False)
    date = models.DateTimeField(auto_now_add=True)
    delrec = models.BooleanField(blank=True, default=False)
    delsen = models.BooleanField(blank=True, default=False)

class Contact(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    userreceiver = models.CharField(max_length=20, blank=True, default='')

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

def create_profil_kin(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        kine_profile = KineProfile(user=user)
        kine_profile.save()
post_save.connect(create_profile, sender=User)


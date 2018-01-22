from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class KineProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    photos = models.ImageField(verbose_name=("Profile Picture"),
                      upload_to="/djangocms/media/", null=True, blank=True)
    Establishment = models.CharField(max_length=100, default='', blank=True)
    Occupation = models.CharField(max_length=100, default='', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

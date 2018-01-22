from django.db import models

# Create your models here.

gender = (
    ('x', 'Male'),
    ('y', 'Female'),
    )

class Questionnaire(models.Model):
      gender = models.CharField(max_length=60, blank=True, default='',choices=gender,verbose_name="gender")

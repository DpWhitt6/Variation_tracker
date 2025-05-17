from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Submission(models.Model):
    Tender = models.Sum('prelims'+'materials'+'labour'+'overheads'+'subcontractors')
    widgets = {
        'prelims': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 15, 'required': True, 'type': 'number',}),
        'material': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 15, 'required': True, 'type': 'number',}), 
        'labour': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 15, 'required': True, 'type': 'number',}),
        'overheads': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 15, 'required': True, 'type': 'number',}),
        'subcontractors': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 15, 'required': True, 'type': 'number',}),
    }
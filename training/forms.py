from dataclasses import fields
from django import forms
from matplotlib.pyplot import cla
from .models import Training

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ["name", "description", "image"]
from django import forms
from .models import Task

class AssignResourceForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_resource']

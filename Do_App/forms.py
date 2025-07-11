from django import forms
from django.forms import ModelForm

from .models import Todo


class AddTaskForm(forms.ModelForm):
    task =forms.CharField(max_length=200,
                          widget=forms.TextInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'task?'
                              }
                          )
                        )
    
    
    class Meta:
        model=Todo
        fields='__all__'
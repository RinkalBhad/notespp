from django import forms
from.models import*

class sign(forms.ModelForm):
    class Meta:
        model=usersingup
        fields='__all__'

class nots(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['query','type_query','comment']

class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'
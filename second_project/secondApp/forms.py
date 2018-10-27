from django import forms
from secondApp.models import Intro
class NewUser(forms.ModelForm):
     class Meta():
        model = Intro
        fields = '__all__'

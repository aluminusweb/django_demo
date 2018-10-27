from django import forms
from django.core import validators

#def check_for_z(value):
#    if value[0] !='z':
#        print(forms.ValidationError("teri ma ki Chu Bot"))
#        raise forms.ValidationError("teri ma ki Chu Bot")
class FormName(forms.Form):
    #name= forms.CharField(validators=[check_for_z])
    name= forms.CharField()
    email= forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required= False , widget= forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    verify_email = forms.EmailField(label = 'Enter email again')
    #def clean_botcatcher(self):
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher)>0:
    #       raise forms.ValidationError("MA ki chu Bot")
    #       return botcatcher

    def clean(self):
        all_clean_data= super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail :
           raise forms.ValidationError("Teri ma ki chu")

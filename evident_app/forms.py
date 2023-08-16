from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class UsercreateForm(UserCreationForm):
   
    email=forms.EmailField(required=True)

    class Meta:
        model=CustomUser
        fields=['first_name','last_name','user_name','email','password1','password2']

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','name':'firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','name':'lastname'}),
             'user_name':forms.TextInput(attrs={'class':'form-control','name':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','name':'email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','name':'password1'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','name':'password2'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  

        self.fields['email'].widget.attrs['class']='form-control'  
        self.fields['password1'].widget.attrs['class']='form-control'  
        self.fields['password2'].widget.attrs['class']='form-control'  
        self.fields['password1'].help_text=''
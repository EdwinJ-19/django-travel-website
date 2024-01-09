from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    f_name = forms.CharField(max_length=20,widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('f_name','email')

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].widget.attrs.update({'autofocus':False})
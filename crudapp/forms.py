from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from.models import Records

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register a user

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1','password2']

    #login user
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#create a record
class CreateRecordForm(forms.ModelForm):
    class Meta:

        model = Records
        fields = ['first_name','last_name','email','phone','address','city','county','country']

class UpdtaeRecordForm(forms.ModelForm):
    class Meta:

        model = Records
        fields = ['first_name','last_name','email','phone','address','city','county','country']
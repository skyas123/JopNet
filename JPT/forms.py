from django import forms
from JPT.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from JPT.models import Persons
from JPT.models import Media
from JPT.models import Posts
from JPT.models import Message
from django.utils.translation import gettext as _


class ava (forms.ModelForm):
    class Meta:
        model=Media
        fields=['photo']
        labels={'photo':'' }
        widgets= {'photo':forms.FileInput(attrs={'style':'display:none','id':'ava','onchange':'document.getElementById("st").click()'})}
       
class PersonsForms (forms.ModelForm):
    class Meta:
        model=Persons
        fields=['size']
        widgets= {'size':forms.NumberInput(attrs={'class': 'form-control'})}

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['text']
        labels={'text':''}
        widgets={

                     'text':forms.Textarea(attrs={
                     'style':'background-color:white',
                     'class':'position-absolute my-4 col-12 rounded-3',
                     'rows':'1',
                     'id':'text',
                     'oninput':'auto_resize(this)'}),
                 }
       
class photo (forms.ModelForm):
    class Meta:
        model=Media
        fields=['photo']
        labels={'photo':'' }
        widgets= {'photo':forms.ClearableFileInput(attrs={'style':'display:none','id':'photo','multiple': True}),}

class messageForm(forms.ModelForm):
    class Meta:
      model=Message
      fields=['text']
      labels={'text':'' }
      widgets={

                     'text':forms.Textarea(attrs={
                     'style':'background-color:white',
                     'class':'position-absolute my-4 col-12 rounded-3',
                     'rows':'1',
                     'id':'text',
                     'oninput':'auto_resize(this)'}),
                 }

class UserForms (forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        widgets= {'password':forms.PasswordInput(attrs={'class':'col-10 offset-1'}),
                  'username':forms.TextInput(attrs={'class':'col-10 offset-1'}),
                  'email':forms.TextInput(attrs={'class':'col-10 offset-1'}),
                  'first_name':forms.TextInput(attrs={'class':'col-10 offset-1'}),
                  'last_name':forms.TextInput(attrs={'class':'col-10 offset-1'})}

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))

    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'}))
                                )

    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_('Just Enter the same password, for confirmation'))

    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
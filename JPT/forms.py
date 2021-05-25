from django import forms
from JPT.models import User
from JPT.models import Persons
from JPT.models import Media
from JPT.models import Posts
from JPT.models import Message

class ava (forms.ModelForm):
    class Meta:
        model=Media
        fields=['photo']
        labels={'photo':'' }
        widgets= {'photo':forms.FileInput(attrs={'style':'display:none','id':'ava','onchange':'document.getElementById("st").click()'})}
       
class PersonsForms (forms.ModelForm):
    class Meta:
        model=Persons
        fields='__all__'

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
        widgets= {'password':forms.PasswordInput(attrs={'class':'col-10 offset-1'}),'username':forms.TextInput(attrs={'class':'col-10 offset-1'})}
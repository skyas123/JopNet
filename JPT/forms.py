from django import forms
from JPT.models import Persons
from JPT.models import Media
from JPT.models import Posts

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
        labels={'text':'' }
        widgets={

                 'text':forms.Textarea(attrs={
                     'style':'background-color:white',
                     'class':'position-absolute top-50 start-50 translate-middle col-12 rounded-3',
                     'rows':'1',
                     'id':'text',
                     'oninput':'auto_resize(this)'}),
                 }
       

class photo (forms.ModelForm):
    class Meta:
        model=Media
        fields=['photo']
        labels={'photo':'' }
        widgets= {'photo':forms.ClearableFileInput(attrs={'style':'display:none','id':'photo','multiple': True})}
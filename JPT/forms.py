from django import forms
from JPT.models import Persons
from JPT.models import Media

class ava (forms.ModelForm):
    class Meta:
        model=Media
        fields=['photo']
        labels={'photo':'' }
        widgets= {'photo':forms.FileInput(attrs={'style':'display:none','id':'ava','onchange':'this.form.submit()'})}
       
class PersonsForms (forms.ModelForm):
    class Meta:
        model=Persons
        fields='__all__'
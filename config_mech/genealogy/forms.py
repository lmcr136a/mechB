from django import forms
from .models import Fost

class FostForm(forms.ModelForm):
    class Meta:
        model=Fost
        fields = ('title','author','content', 'file')


    def __init__(self, *args, **kwargs):
        super(FostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False



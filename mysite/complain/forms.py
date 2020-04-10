from django import forms
from .models import Complain


class CreateComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = '__all__'
        #fields = [ 'title', 'description', 'date']

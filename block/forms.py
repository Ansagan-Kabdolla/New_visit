from django import forms
from .models import Zakaz

class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ('organization','name','first_period','second_period','iin','password')

from django import forms
from .models import Handin


class HandinForm(forms.ModelForm):
    class Meta:
        model = Handin
        fields = ['holder', 'attached_files', 'assignment']

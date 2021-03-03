from django import forms
from .models import Handin


class HandinForm(forms.Form):
    class Meta:
        model = Handin
        fields = ['holder', 'attached_files', 'assignment_type']

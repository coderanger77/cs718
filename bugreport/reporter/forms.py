from django import forms

from .models import Bug


class BugCreateForm(forms.ModelForm):

    class Meta:
        model=Bug
        fields=['title','description']


class BugUpdateForm(forms.ModelForm):

    class Meta:
        model=Bug
        fields=['bugId','title','description'] #add any fields that needs to be updated.

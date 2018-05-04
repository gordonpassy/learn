from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Subject Name'})
        }
        fields = ('name',)

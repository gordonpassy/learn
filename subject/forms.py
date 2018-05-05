from django import forms
from .models import Subject, Chapter


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Subject name'})
        }
        fields = ('name',)


class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Chapter title'})
        }
        fields = ('title',)

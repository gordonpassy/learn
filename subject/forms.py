from django import forms
from .models import Subject, Chapter, Topic


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
            'title': forms.TextInput(attrs={'placeholder': 'Chapter title'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Chapter number'})
        }
        fields = ('number', 'title',)


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Topic title'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Topic number'})
        }
        fields = ('number', 'title',)

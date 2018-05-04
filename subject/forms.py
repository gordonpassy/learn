from django import forms
from django.utils.text import slugify
from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Subject Name'})
        }
        fields = ('name',)

    def save(self):
        instance = super(SubjectForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()

        return instance

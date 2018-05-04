from django.shortcuts import render
from .forms import SubjectForm

# Create your views here.


def index(request):
    title = 'Home page'
    form = SubjectForm()
    args = {"title": title, "subject_form": form}
    return render(request, "subjects/index.html", args)

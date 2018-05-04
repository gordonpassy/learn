from django.shortcuts import render, redirect
from .forms import SubjectForm
from .models import Subject

# Create your views here.


def index(request):
    title = 'Home page'
    subjects = Subject.objects.all()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.author = request.user
            subject.save()
            return redirect('homepage')
    else:
        form = SubjectForm()
    args = {"title": title, "subject_form": form, "subjects": subjects}
    return render(request, "subjects/index.html", args)

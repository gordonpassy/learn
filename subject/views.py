from django.shortcuts import get_object_or_404, render, redirect
from .forms import SubjectForm
from .models import Subject

# Create your views here.


def index(request):
    title = 'Home page'
    subjects = Subject.objects.all()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save()
            subject.author = request.user
            subject.save()
            return redirect('subject:homepage')
    else:
        form = SubjectForm()
    args = {"title": title, "subject_form": form, "subjects": subjects}
    return render(request, "subjects/index.html", args)


def subject_chapters(request, id, subject_slug):
    subject = get_object_or_404(Subject, id=id, slug=subject_slug)
    title = subject
    args = {"subject": subject, "title": title}
    return render(request, "subjects/subject_chapters.html", args)

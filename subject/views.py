from django.shortcuts import get_object_or_404, render, redirect
from .forms import SubjectForm, ChapterForm
from .models import Subject, Chapter
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
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


def subject_chapters(request, id):
    subject = get_object_or_404(Subject, id=id)
    chapters = Chapter.objects.filter(subject_id=id)
    title = subject
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save()
            chapter.author = request.user
            chapter.subject = subject
            chapter.save()
            return redirect("subject:subject_chapters", id=subject.id)
    else:
        form = ChapterForm()
    args = {"subject": subject, "title": title, "chapter_form": form, "subject_chapters": chapters}

    return render(request, "subjects/subject_chapters.html", args)

from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Home page'
    args = {"title": title}
    return render(request, "subjects/index.html", args)

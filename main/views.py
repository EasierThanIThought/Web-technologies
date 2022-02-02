from django.shortcuts import render, redirect
from .forms import FeedBackForm


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def message(request):
    error = ''
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
        else:
            error = 'Форма заполнена неверно'
    form = FeedBackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/message.html", context)

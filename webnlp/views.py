from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {

    })


def regex(request):
    return render(request, 'regex.html', {

    })


def lemo(request):
    return render(request, 'lemo.html', {

    })


def pos(request):
    return render(request, 'pos.html', {

    })


def ner(request):
    return render(request, 'ner.html', {

    })

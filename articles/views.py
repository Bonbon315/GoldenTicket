from django.shortcuts import render


def main(request):
    return render(request, "articles/main.html")


def index(request):
    return render(request, "articles/index.html")
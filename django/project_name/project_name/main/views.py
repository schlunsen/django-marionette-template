from django.shortcuts import render, redirect 


def home(request):
    ctx = {}
    return render(request, "index.html", ctx)

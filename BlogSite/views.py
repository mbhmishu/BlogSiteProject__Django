from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponseRedirect(reverse('blogapp:blogs'))
    
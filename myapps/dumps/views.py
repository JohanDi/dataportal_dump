from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

# Create your views here.


def overview(request):

    context = {'title': 'Geert is een toffe peer.'}
    response = render_to_string('main.html', context=context)
    return HttpResponse(response)


def dump1(request):

    pass






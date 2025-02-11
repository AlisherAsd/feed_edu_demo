from django.http import HttpResponse
from django.shortcuts import render
from docutils.nodes import title

def index(request):
    return render(request, 'feed_edu_demo/index.html')
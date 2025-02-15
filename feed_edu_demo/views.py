from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    if (request.user.is_authenticated == True):
        return redirect("user_dashboard")
    else:
        return render(request, 'feed_edu_demo/index.html')
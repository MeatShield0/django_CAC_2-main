from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def event(request):
    return render(request,"ClubNexus\event.html")


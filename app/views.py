from django.shortcuts import render
from app.models import *

def display_topic(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QSA=AccessRecords.objects.all()
    d={'access':QSA}
    return render (request,'display_access.html',d)


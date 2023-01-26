from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def display_topic(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='kabaddi')
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by(Length('topic_name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all().order_by(Length('topic_name'))
    QSW=Webpage.objects.all().order_by(Length('url'))
    QSW=Webpage.objects.all().order_by(Length('topic_name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith="com")
    QSW=Webpage.objects.filter(name__startswith='s')
    QSW=Webpage.objects.filter(url__contains='a')
    QSW=Webpage.objects.filter(Q(topic_name='cricket') | Q(name='suresh'))
    QSW=Webpage.objects.filter(Q(name__startswith='s') & Q(name__endswith='h'))
    QSW=Webpage.objects.filter(name__in=['suresh','Dhoni','mathaiah'])
    QSW=Webpage.objects.exclude(name__startswith='s')

    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='1998')
    QSA=AccessRecords.objects.filter(date__month='9')
    QSA=AccessRecords.objects.filter(date__day='10')
    QSA=AccessRecords.objects.filter(date__day='23')
    QSA=AccessRecords.objects.filter(date__year__lte='2000')
    QSA=AccessRecords.objects.filter(date__year__gte='1999')
    d={'access':QSA}
    return render (request,'display_access.html',d)


from django.shortcuts import render

from app.models import *
from django.http import HttpResponse
# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)

def insert_topic(request):
    tn=input('enter topic name :')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is inserted Successfully')

def insert_webpage(request):
    tn=input('Enter topic name :')
    name=input('Enter name :')
    url=input('Enter url :')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('Webpage data is Insertedb Successfully')
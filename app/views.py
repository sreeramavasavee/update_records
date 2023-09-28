from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    t=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    return HttpResponse('inserted successfully...')

def display(request):
    qsro=topic.objects.all()
    d={'qsro':qsro}
    return render(request,'display.html',d)

def update_topic(request):
    otn = input('old topic name: ')
    ntn=input('new topic name : ')
    topic.objects.filter(topic_name=otn).update(topic_name=ntn)
    return HttpResponse('updated')

def insert_webpage(request):
    t=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    name=input('enter a name:')
    url=input('enter url:')
    no=webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
    no.save()
    return HttpResponse('data inserted successfully..')

def update_webpage(request):
    own=input('enter old name: ')
    new=input('enter new name: ')
    webpage.objects.filter(name=own).update(name=new)
    return HttpResponse('updated successfully')

def display_webpage(request):
    wsro=webpage.objects.all()
    d={'wsro':wsro}
    return render(request,'display_webpage.html',d)

def insert_accessrecords(request):
    t=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    name=input('enter a name:')
    url=input('enter url:')
    no=webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
    no.save()
    date=input('enter date:')
    author=input('enter author:')
    aro=accessrecords.objects.get_or_create(name=no,date=date,author=author)[0]
    aro.save()
    return HttpResponse('inserted data to accessrcords successfully..')

def display_accessrecords(request):
    asro=accessrecords.objects.all()
    d={'asro':asro}
    return render(request,'display_accessrecords.html',d)

def update_accessrecords(request):
    old=input('enter old authorname:')
    new=input('enter new authorname:')
    accessrecords.objects.filter(author=old).update(author=new)
    return HttpResponse('updated successfully')

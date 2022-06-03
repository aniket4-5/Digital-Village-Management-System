from django.shortcuts import render
from django.http import HttpResponse
from villageapp.models import Notification


def home(req):

    return render(req, 'villageapp/index.html', {'complaints': complaints})


def about(req):
    return render(req, 'villageapp/about.html')


def notification(req):

    data = Notification.objects.all()
    return render(req, 'villageapp/notification.html', {'data': data})


def jobs(req):
    return render(req, 'villageapp/jobs.html')


def complaints(req):
    return render(req, 'villageapp/complaints.html')

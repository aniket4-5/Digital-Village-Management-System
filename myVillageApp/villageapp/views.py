from django.shortcuts import render
from django.http import HttpResponse

complaints = [

    {
        'author': 'XYZ',
        'title': 'ABc Cde',
        'Desc': 'sghsgd  fjshfj  sjfhdkjs  shfkjs ',
        'date-posted': 'hjsdkjfh  shfkf'

    },
    {
        'author': 'XYZ',
        'title': 'ABc Cde',
        'Desc': 'sghsgd  fjshfj  sjfhdkjs  shfkjs ',
        'date-posted': 'hjsdkjfh  shfkf'

    },
    {
        'author': 'XYZ',
        'title': 'ABc Cde',
        'Desc': 'sghsgd  fjshfj  sjfhdkjs  shfkjs ',
        'dateposted': 'hjsdkjfh  shfkf'
    }
]


def home(req):
   
    return render(req, 'villageapp/index.html',{'complaints':complaints})


def about(req):
    return render(req, 'villageapp/about.html')

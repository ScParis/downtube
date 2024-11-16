from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    #html = f'<html><body><H1>It is now {now}</H1></body></html>'
    return render(request, 'contas/home.html')

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib import messages


def index(request):    
        return render(request, 'index.html', {})


def sendwatt(request):  
        request.encoding='utf-8'
        if 'q' in request.GET:
            js_alert = 'WhattsApp Enviado.'	
        else:	
            js_alert = 'WhattsApp Enviado.'
        return render('index.html', {"my_alert": js_alert})
        
	#return render(request, 'index.html', {})



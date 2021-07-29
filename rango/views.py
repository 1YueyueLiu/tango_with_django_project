from typing import ContextManager
from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category


def index(request):
     #construct a dictionary to pass to the template engine as its context
     category_list = Category.objects.order_by('-likes')[:5]
     context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
     #return a rendered response to send to the client
     return render(request, 'rango/index.html', context=context_dict)
     

#def index(request):
 #    return HttpResponse('Rango says hey there partner!'+'<a href=\'/rango/about/\'>About</a>')

#def about(request):
 #    return HttpResponse('Rango says here is the about page.'+'<a href=\'/rango/\'>Index</a>')
def about(request):
     context1 = {'yourname':'Yueyue Liu'}
     return render(request, 'rango/about.html', context= context1)
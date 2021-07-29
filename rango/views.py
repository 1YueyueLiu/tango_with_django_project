from typing import ContextManager
from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
     #construct a dictionary to pass to the template engine as its context
     category_list = Category.objects.order_by('-likes')[:5]
     page_list=Page.objects.order_by('-views')[:5]
     context_dict = {}
     context_dict['categories'] = category_list
     context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake '
     context_dict['pages'] = page_list
     #return a rendered response to send to the client
     return render(request, 'rango/index.html', context=context_dict)
     

#def index(request):
 #    return HttpResponse('Rango says hey there partner!'+'<a href=\'/rango/about/\'>About</a>')

#def about(request):
 #    return HttpResponse('Rango says here is the about page.'+'<a href=\'/rango/\'>Index</a>')
def about(request):
     context1 = {'yourname':'Yueyue Liu'}
     return render(request, 'rango/about.html', context= context1)


def show_category(request, category_name_slug):
         context_dict = {}
         try:
              category = Category.objects.get(slug=category_name_slug)
              pages = Page.objects.filter(category=category)
              context_dict['pages'] = pages
              context_dict['category'] = category
         except  Category.DoesNotExist:
              context_dict['category'] = None
              context_dict['pages'] = None
         return render(request, 'rango/category.html', context= context_dict)
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.views.generic.detail import DetailView
from .models import About,Teachers,Blog


def homepage(request):
    return render(request,'homepage.html')

class About(ListView):
    model=About
    template_name='about.html'

class Teacher(ListView):
    model=Teachers
    template_name='teachers.html'

class Blog(ListView):
    ordering='-vaqt'
    model=Blog
    template_name='blog.html'

class Create(CreateView):
    model=Blog
    template_name='create.html'
    fields=['matn','sarlafha']
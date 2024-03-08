from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , ListView
from .models import Post

# Create your views here.
'''class Home(TemplateView):
    template_name='home.html' '''

class Home(ListView):
    model = Post
    template_name='home.html'
    context_object_name ='all_posts'


class About(TemplateView):
    template_name='about.html'

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.
class IndexView(TemplateView):
   template_name = "index.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["data"] = "Site under construction, come back soon..."
       context["title"] = "Home"
       return context
   

class ProjectListView(ListView):
   context_object_name = "projects"
   model = models.Project
   template_name = "projects_overview.html"
   ordering = ['order']

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["title"] = "Projects"
       return context
   

class AboutMeView(TemplateView):
   template_name = "aboutme.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["title"] = "About Me"
       return context
   

class ContactView(TemplateView):
   template_name = "contact.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["title"] = "Contact"
       return context
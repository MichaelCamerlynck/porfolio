from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
   template_name = "index.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["data"] = "Site under construction, come back soon..."
       context["title"] = "Home"
       return context
   

class ProjectView(TemplateView):
   template_name = "projects_overview.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context
   

class AboutMeView(TemplateView):
   template_name = "aboutme.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context
   

class ContactView(TemplateView):
   template_name = "contact.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context
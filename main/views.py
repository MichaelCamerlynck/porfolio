from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
import requests
from . import models
from .models import Project

# Create your views here.
class IndexView(TemplateView):
   template_name = "index.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["data"] = "Site under construction, come back soon..."
       context["title"] = "Home"
       return context
   

class ProjectListView(ListView):
   model = models.Project
   template_name = "projects_overview.html"
   ordering = ['order']
   context_object_name = 'projects'

   def get_queryset(self):
        return Project.objects.filter(show=True).order_by("order")

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["title"] = "Projects"
       return context
   
class ProjectDetailView(DetailView):
    model = models.Project
    template_name = "project.html"

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       project = self.get_object()
       context["title"] = project.name
       context["summary"] = project.summary.split("||||")
       context["techical"] = project.techical_detail.split("||||")
       context["roles"] = project.roles.split("||||")
       context["roles_list"] = project.roles_list.split("||||")
       context["challenges"] = project.challenges.split("||||")
       context["results"] = project.results.split("||||")
       context["main_img"] = project.img_set.filter(position='main').first()
       context["techical_img"] = project.img_set.filter(position='techical').all()
       context["roles_img"] = project.img_set.filter(position='roles').all()
       context["challenges_img"] = project.img_set.filter(position='challenges').all()
       context["results_img"] = project.img_set.filter(position='results').all()
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
   
   
def send(request):
    name = request.GET["name"]
    email = request.GET["email"]
    subject = request.GET["subject"]
    message = request.GET["message"]
    formatted_message = f"<@622098365806542868>\n" \
                        f"```\n" \
                        f"New message \n" \
                        f"Name: {name} \n" \
                        f"Email: {email} \n" \
                        f"Subject: {subject}\n" \
                        f"Message: \n" \
                        f"{message}\n" \
                        f"```"

    if name == "" or email == "" or subject == "" or message == "":
        return JsonResponse({"data" : "invalid"}, status=200)

    data = {
        "content": formatted_message
    }

    url = "https://discord.com/api/webhooks/1073698819985899592/MC7ZyK72W0X-5mqAJSf8GqNqVF_FVFeMlu-Konkj50GDK7HiM1PiCFr883qg7zA1waxf"
    requests.post(url, json=data)

    return JsonResponse({"data" : "success"}, status=200)
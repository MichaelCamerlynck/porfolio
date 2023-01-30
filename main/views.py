from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(response):
    return render(response, "index.html")

class IndexView(TemplateView):
   template_name = "index.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["data"] = "Site under construction, come back soon..."
       context["title"] = "Site Under Construction"
       return context
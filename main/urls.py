from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("projects", views.ProjectView.as_view(), name='projects'),
    path("contactme", views.ContactView.as_view(), name='contactme'),
    path("aboutme", views.AboutMeView.as_view(), name='aboutme'),
]
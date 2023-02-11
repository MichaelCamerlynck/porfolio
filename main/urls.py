from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("projects", views.ProjectListView.as_view(), name='projects'),
    path("project/<int:pk>", views.ProjectDetailView.as_view(), name='project'),
    path("contactme", views.ContactView.as_view(), name='contactme'),
    path("aboutme", views.AboutMeView.as_view(), name='aboutme'),
    path("send", views.send, name='send'),
]
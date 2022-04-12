from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "project"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.project_listing, name="project"),
    path("<slug:id>/", views.project_detail, name="project_detail"),
    path("project/new", views.create_project),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

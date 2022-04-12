from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from guardian.shortcuts import get_objects_for_user

from .forms import ImageForm, ProjectForm
from .models import Image, Project


def index(request):
    return render(request, "index.html")


@login_required
@permission_required("project.view_project")
def project_listing(request):
    project_data = get_objects_for_user(
        request.user, "project.dg_view_project", klass=Project
    )
    return render(request, "project.html", {"projects": project_data})


@login_required
@permission_required("project.view_project")
def project_detail(request, id):
    project = get_object_or_404(Project, slug=id)
    return render(request, "detail.html", {"detail": project})


def create_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return HttpResponseRedirect(reverse("project:project"))
    else:
        form = ProjectForm()

    return render(request, "create_project.html", {"form": form})
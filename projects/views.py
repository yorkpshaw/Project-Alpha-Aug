from django.shortcuts import render
from django.views.generic.list import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projectslist"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

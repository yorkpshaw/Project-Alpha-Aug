from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from tasks.models import Task
from django.urls import reverse_lazy
from django.views.generic.list import ListView


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/mine.html"
    context_object_name = "task_list"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    context_object_name = "taskupdate"
    success_url = reverse_lazy("show_my_tasks")
    fields = ["is_completed"]

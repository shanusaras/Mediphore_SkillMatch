from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from .models import *

# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskDetails.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.object  # current task

        # Filter resources that match at least one required skill AND are available
        matching_resources = Resource.objects.filter(
            skills__in=task.required_skills.all(),
            availabilities__start_time__lte=task.start_time,
            availabilities__end_time__gte=task.end_time,
            availabilities__status='available'
        ).distinct()

        # Add to context
        context['matching_resources'] = matching_resources
        return context

class AssignResourceView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        resource_id = request.POST.get("resource_list")
        if resource_id:
            resource = get_object_or_404(Resource, id=resource_id)
            # Assign resource to task
            task.assigned_resource = resource
            task.status = 'in_progress'
            task.save()

            # Update resource availability for the task duration
            availability = ResourceAvailability.objects.filter(
                resource=resource,
                start_time__lte=task.start_time,
                end_time__gte=task.end_time,
                status="available"
            ).first()

            if availability:
                availability.status = "unavailable"
                availability.save()

        return redirect("task-detail", pk=task.pk)  # back to detail page

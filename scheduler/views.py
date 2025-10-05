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

class ProjectTaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Task.objects.filter(project_id=project_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        context['project'] = get_object_or_404(Project, id=project_id)
        return context

# Handles GET requests to display task details and available resources
class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskDetails.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.object  # current task

        # Get IDs of resources already assigned to other tasks during this time
        assigned_resource_ids = Task.objects.filter(
            start_time__lt=task.end_time,
            end_time__gt=task.start_time,
            assigned_resource__isnull=False  # Only consider tasks with assigned resources
        ).exclude(pk=task.pk).values_list('assigned_resource', flat=True)

        # Filter available resources, excluding already assigned ones
        matching_resources = Resource.objects.filter(
            skills__in=task.required_skills.all(),
            availabilities__start_time__lte=task.start_time,
            availabilities__end_time__gte=task.end_time,
            availabilities__status='available'
        ).exclude(id__in=assigned_resource_ids).distinct()

        context['matching_resources'] = matching_resources
        return context

        # Ensure resource has ALL required skills
        # for skill in task.required_skills.all():
        #     matching_resources = matching_resources.filter(skills=skill)

# Handles POST requests to assign a resource to a task
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

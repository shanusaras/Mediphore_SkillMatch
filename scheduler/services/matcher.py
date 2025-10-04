from django.db.models import Q
from rest_framework.exceptions import ValidationError
from ..models import Task, Resource, ResourceAvailability

def resources_for_task(task, top_n=3):
    """
    Simple resource matcher for tasks.
    Returns available resources with required skills.
    """
    if not task or not hasattr(task, 'required_skills'):
        return []

    try:
        # Get resources with at least one required skill
        resources = Resource.objects.filter(
            skills__in=task.required_skills.all()
        ).distinct()

        available_resources = []
        for resource in resources:
            # Check availability
            is_available = not ResourceAvailability.objects.filter(
                resource=resource,
                start_time__lt=task.end_time,
                end_time__gt=task.start_time,
                status='unavailable'
            ).exists()

            if is_available:
                available_resources.append({
                    'id': resource.id,
                    'name': resource.name,
                    'email': resource.email,
                    'skills': list(resource.skills.values_list('name', flat=True))
                })

        return available_resources[:top_n]

    except Exception as e:
        raise ValidationError(f"Error finding resources: {str(e)}")

def match_for_project(project_id, top_n_per_task=3):
    """
    Simple project resource matcher.
    Returns resources for each task in the project.
    """
    from ..models import Project
    
    try:
        project = Project.objects.get(id=project_id)
        results = {}
        
        for task in project.tasks.all():
            results[str(task.id)] = resources_for_task(task, top_n_per_task)
            
        return results
        
    except Project.DoesNotExist:
        raise ValidationError("Project not found")
    except Exception as e:
        raise ValidationError(f"Error in project matching: {str(e)}")
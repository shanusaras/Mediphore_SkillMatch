from django.contrib import admin
from .models import *

# Create a custom admin configuration just for the Task model and Resource model
# Slightly enhanced with better many-to-many handling
class TaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('required_skills',)

class ResourceAdmin(admin.ModelAdmin):
    filter_horizontal = ('skills',)

# Register models
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceAvailability)
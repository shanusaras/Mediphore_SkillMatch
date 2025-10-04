from rest_framework import serializers
from .models import Skill, Resource, ResourceAvailability, Task, Project, ResourceAssignment

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Resource
        fields = ['id', 'name', 'email', 'skills', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 
                 'created_at', 'updated_at', 'tasks']

class TaskSerializer(serializers.ModelSerializer):
    required_skills = SkillSerializer(many=True, read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'project', 'required_skills', 
                 'start_time', 'end_time', 'status', 'created_at', 'updated_at']

class ResourceAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceAvailability
        fields = '__all__'

class ResourceAssignmentSerializer(serializers.ModelSerializer):
    resource = ResourceSerializer(read_only=True)
    task = TaskSerializer(read_only=True)
    
    class Meta:
        model = ResourceAssignment
        fields = '__all__'
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from scheduler.models import Project, Task, Resource, Skill, ResourceAvailability
from scheduler.services.matcher import resources_for_task

class TestMatcher(TestCase):
    def setUp(self):
        # Create a skill
        self.python = Skill.objects.create(name="Python")
        
        # Create a project
        self.project1 = Project.objects.create(
            name="Test Project",
            start_date="2023-01-01",
            end_date="2023-12-31"
        )
        
        # Create a resource
        self.dev1 = Resource.objects.create(name="Python Dev", email="py@example.com")
        self.dev1.skills.add(self.python)
        
        # Set availability
        now = timezone.now()
        ResourceAvailability.objects.create(
            resource=self.dev1,
            start_time=now,
            end_time=now + timedelta(days=10),
            status="available"
        )

    def test_simple_matching(self):
        task = Task.objects.create(
            name="Simple Task",
            project=self.project1,
            start_time=timezone.now() + timedelta(days=1),
            end_time=timezone.now() + timedelta(days=2)
        )
        task.required_skills.add(self.python)
        
        matches = resources_for_task(task)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]['name'], 'Python Dev')
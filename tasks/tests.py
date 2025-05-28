from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title="Test Task", description="Test Description")

    def test_task_content(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")

class TaskViewsTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Another Task", description="Some desc")

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another Task")

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some desc")
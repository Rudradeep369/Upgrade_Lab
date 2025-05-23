from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Repository(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Commit(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.message} - {self.author.username}"

class RepositoryFile(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    file = models.FileField(upload_to='repositories/', max_length=1000)
    path = models.CharField(max_length=1000)

    def __str__(self):
        return self.path

class ProjectReport(models.Model):
    repository = models.OneToOneField(Repository, on_delete=models.CASCADE, related_name='project_report')
    file = models.FileField(upload_to='project_reports/', max_length=1000)

    def __str__(self):
        return f"Report for {self.repository.name}"
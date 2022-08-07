from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['complete']
    
    def get_absolute_url(self):
        return reverse("tasks")
    
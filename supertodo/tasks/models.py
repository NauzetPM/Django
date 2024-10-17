from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    complete_before = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

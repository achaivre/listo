from django.db import models
from django.contrib.auth.models import User

# from django import forms

PRIORITY_CHOICES = (("high", "HIGH"), ("medium", "MEDIUM"), ("low", "LOW"))
CATEGORY_CHOICES = (("grocery", "GROCERY"), ("none", "NONE"))

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="")

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = "user"


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default="low")
    created = models.DateTimeField(auto_now_add=True)
    task_list = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = "user"

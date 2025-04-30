from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)

    def __str__(self):
        return f"{self.name}"

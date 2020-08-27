from django.db import models

class employee(models.Model):
    name = models.CharField(max_length = 10)
    Salary = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()

    def __str__(self):
        return self.name
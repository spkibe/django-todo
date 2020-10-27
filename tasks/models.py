from django.db import models

# Create your models here.
class Task(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=50)
    #dateline = 

    def __str__(self):
        return self.task
    
from django.db import models

# Create your models here.
class Complain(models.Model):
    student_name = models.CharField(max_length=128, null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Complain(models.Model):
    student_name = models.Charfield(max_length=128, null=True, blank=True)
    title = models.Charfield(max_length=64)
    description = models.Textfield()
    date= models.Textfield()


    def __str__(self):
        return self.title
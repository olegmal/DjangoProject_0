from django.db import models


class Teacher(models.Model):

    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=155)
    start_date = models.DateField()
    subject = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}, getting started: {self.start_date}'

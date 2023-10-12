from django.db import models


class Group(models.Model):

    name_of_curator = models.CharField(max_length=120, blank=True, null=True)
    name_of_teacher = models.CharField(max_length=120)
    code_number = models.PositiveSmallIntegerField()
    subject = models.CharField(max_length=50)
    quantity_of_students = models.PositiveSmallIntegerField()
    start_date = models.DateField(null=True)

    def __str__(self):
        return (f'Предмет: {self.subject}, куратор:{self.name_of_curator} викладач: {self.name_of_teacher}, \n'
                f'код групи: {self.code_number}, середній бал - {self.start_date}')

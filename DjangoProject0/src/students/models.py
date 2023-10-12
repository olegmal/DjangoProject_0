import random
from django.db import models
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=155)
    grade = models.PositiveSmallIntegerField(default=0, null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}, grade: {self.grade}, birth_date: {self.birth_date}'

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                grade=random.randint(1, 100),
                birth_date=faker.date_time_between(
                    start_date="-30y", end_date="-18y")
            )
            # student.email = faker.email  # альтернативний синтаксис

# Generated by Django 4.2.6 on 2023-10-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_curator', models.CharField(blank=True, max_length=120, null=True)),
                ('name_of_teacher', models.CharField(max_length=120)),
                ('code_number', models.PositiveSmallIntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('average_score', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=155)),
                ('getting_started', models.DateField()),
                ('subject', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.0 on 2021-12-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empl', '0002_rename_employee_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='location',
            field=models.CharField(default='python', max_length=100),
        ),
    ]

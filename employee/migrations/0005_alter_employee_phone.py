# Generated by Django 4.2.2 on 2023-07-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_remove_employee_dept_remove_employee_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dept_name',
            new_name='dept',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(default='', max_length=500),
        ),
    ]

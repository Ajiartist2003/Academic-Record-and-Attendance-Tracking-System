# Generated by Django 4.1.7 on 2023-03-11 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_student_bus_route_no_student_mode_of_transpotation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='Employee_name',
            new_name='name',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_name_staff_employee_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Bus_route_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Mode_of_Transpotation',
            field=models.CharField(choices=[('College bus', 'College bus'), ('Own vehicle', 'Own vehicle'), ('By walk', 'By walk')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Regular_dropping_point',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Rugular_Boarding_point',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

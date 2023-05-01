# Generated by Django 4.1.7 on 2023-03-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_studentattendance_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentattendance',
            name='period',
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_1',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_2',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_3',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_4',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_5',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_6',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_7',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='period_8',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100, null=True),
        ),
    ]

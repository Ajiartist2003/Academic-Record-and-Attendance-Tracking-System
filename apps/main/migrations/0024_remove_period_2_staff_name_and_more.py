# Generated by Django 4.1.7 on 2023-03-16 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_period_8_period_7_period_6_period_5_period_4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period_2',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_2',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='period_3',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_3',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='period_4',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_4',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='period_5',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_5',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='period_6',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_6',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='period_7',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_7',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='period_8',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='period_8',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_1',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_2',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_3',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_4',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_5',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_6',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_7',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='period_8',
        ),
        migrations.AddField(
            model_name='timetable',
            name='period',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eight', 'Eight')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='staff_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.staff'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='subject_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject'),
        ),
        migrations.DeleteModel(
            name='Period_1',
        ),
        migrations.DeleteModel(
            name='Period_2',
        ),
        migrations.DeleteModel(
            name='Period_3',
        ),
        migrations.DeleteModel(
            name='Period_4',
        ),
        migrations.DeleteModel(
            name='Period_5',
        ),
        migrations.DeleteModel(
            name='Period_6',
        ),
        migrations.DeleteModel(
            name='Period_7',
        ),
        migrations.DeleteModel(
            name='Period_8',
        ),
    ]

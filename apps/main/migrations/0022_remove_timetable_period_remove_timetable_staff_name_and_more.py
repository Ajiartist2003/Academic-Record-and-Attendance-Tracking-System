# Generated by Django 4.1.7 on 2023-03-16 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_timetable_day_alter_timetable_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='period',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='staff_name',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='subject_name',
        ),
        migrations.CreateModel(
            name='Period_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.staff')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Period_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.staff')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Period_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.staff')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
            ],
        ),
        migrations.AddField(
            model_name='timetable',
            name='period_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.period_1'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='period_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.period_2'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='period_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.period_3'),
        ),
    ]
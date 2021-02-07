# Generated by Django 3.1.6 on 2021-02-03 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_assignedcourses_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammeCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.course')),
                ('programme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.programme')),
            ],
        ),
    ]
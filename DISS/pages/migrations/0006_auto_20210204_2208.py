# Generated by Django 3.1.6 on 2021-02-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_programmecourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='final_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='starting_score',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 5.1 on 2024-10-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0007_alter_submission_submission_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='solved_problems',
            field=models.ManyToManyField(blank=True, related_name='solved_by', to='coding.problem'),
        ),
    ]

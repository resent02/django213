# Generated by Django 3.0.3 on 2020-02-26 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_mentor_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mentor',
        ),
    ]

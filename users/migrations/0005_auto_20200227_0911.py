# Generated by Django 3.0.3 on 2020-02-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200226_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

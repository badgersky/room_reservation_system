# Generated by Django 4.1.7 on 2023-03-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_volunteers_delete_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='registration',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_volunteers_date_alter_volunteers_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='skills',
            field=models.CharField(max_length=50),
        ),
    ]

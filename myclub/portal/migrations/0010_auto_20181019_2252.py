# Generated by Django 2.1.2 on 2018-10-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20181019_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
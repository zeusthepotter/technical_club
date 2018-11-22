# Generated by Django 2.1.2 on 2018-11-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_auto_20181107_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='branch',
            field=models.CharField(blank=True, choices=[('CSE', 'CSE'), ('CE', 'CE'), ('EL', 'EL'), ('EE', 'EE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, choices=[('Volunteer', 'Volunteer'), ('Coordinator', 'Coordinator'), ('Assistant Coordinator', 'Assistant Coordinator')], max_length=30, null=True),
        ),
    ]
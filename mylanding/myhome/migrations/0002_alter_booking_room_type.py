# Generated by Django 5.1.1 on 2024-11-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(choices=[('standard', 'Standard'), ('executive', 'Executive')], max_length=20),
        ),
    ]
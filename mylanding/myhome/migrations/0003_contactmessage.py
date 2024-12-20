# Generated by Django 5.1.1 on 2024-11-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0002_alter_booking_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-15 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evident_app', '0004_inputvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputvalue',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputvalue',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 3.2.6 on 2023-08-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='access_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
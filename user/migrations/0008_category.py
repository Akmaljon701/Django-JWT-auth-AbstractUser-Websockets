# Generated by Django 3.2.6 on 2023-09-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_ism_rasm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='categories/')),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='url',
            field=models.CharField(default='', max_length=300),
        ),
    ]
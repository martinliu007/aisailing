# Generated by Django 4.2.1 on 2023-06-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_app_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
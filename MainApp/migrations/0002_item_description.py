# Generated by Django 4.2.13 on 2024-06-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='Описания ещё нет', max_length=512),
        ),
    ]
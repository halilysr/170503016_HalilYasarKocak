# Generated by Django 4.0.4 on 2022-04-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='training',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

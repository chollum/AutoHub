# Generated by Django 2.1.4 on 2019-01-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='humidity',
            field=models.CharField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(default='Generic room', max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='room',
            name='temperature',
            field=models.CharField(default=0, max_length=5),
        ),
    ]

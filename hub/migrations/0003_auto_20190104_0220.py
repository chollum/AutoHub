# Generated by Django 2.1.4 on 2019-01-04 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_auto_20190103_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='tag',
        ),
    ]

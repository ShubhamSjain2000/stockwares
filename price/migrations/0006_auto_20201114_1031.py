# Generated by Django 3.1.2 on 2020-11-14 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_auto_20201114_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indices',
            old_name='open',
            new_name='opens',
        ),
    ]
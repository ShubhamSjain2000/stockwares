# Generated by Django 3.1.2 on 2020-11-14 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0007_auto_20201114_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indices',
            name='op',
        ),
    ]

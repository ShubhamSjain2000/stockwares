# Generated by Django 3.1.2 on 2020-11-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0008_remove_indices_op'),
    ]

    operations = [
        migrations.AddField(
            model_name='indices',
            name='fact',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

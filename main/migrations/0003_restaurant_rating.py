# Generated by Django 4.1.1 on 2022-11-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

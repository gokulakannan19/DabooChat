# Generated by Django 3.1 on 2020-09-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200907_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('send', 'send')], max_length=8),
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-28 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typerforum', '0008_alter_post_car_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]

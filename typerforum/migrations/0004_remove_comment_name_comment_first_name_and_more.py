# Generated by Django 4.2.6 on 2023-10-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typerforum', '0003_auto_20231014_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

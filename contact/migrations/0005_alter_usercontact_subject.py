# Generated by Django 4.2.6 on 2023-12-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_rename_message_content_usercontact_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]

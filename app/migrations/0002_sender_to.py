# Generated by Django 3.1.3 on 2020-12-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sender',
            name='to',
            field=models.CharField(default='user1', max_length=30),
        ),
    ]

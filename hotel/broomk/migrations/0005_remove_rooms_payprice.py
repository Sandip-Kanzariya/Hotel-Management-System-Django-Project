# Generated by Django 4.1.5 on 2023-03-31 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broomk', '0004_rooms_payprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='payprice',
        ),
    ]
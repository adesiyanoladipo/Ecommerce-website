# Generated by Django 3.2.8 on 2021-10-13 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211012_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone_Number',
            new_name='number',
        ),
    ]

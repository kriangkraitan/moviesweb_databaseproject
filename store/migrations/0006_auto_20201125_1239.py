# Generated by Django 3.1.2 on 2020-11-25 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201125_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='username',
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-26 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_finch_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='beak_shape',
            new_name='beak_type',
        ),
    ]

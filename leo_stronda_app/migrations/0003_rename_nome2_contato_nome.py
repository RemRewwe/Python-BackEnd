# Generated by Django 5.2.1 on 2025-05-29 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leo_stronda_app', '0002_contato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='nome2',
            new_name='nome',
        ),
    ]

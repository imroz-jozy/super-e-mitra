# Generated by Django 5.0 on 2024-01-16 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formfill', '0003_rename_from_details_userform_from_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userform',
            old_name='from_name',
            new_name='form_name',
        ),
    ]

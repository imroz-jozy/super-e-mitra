# Generated by Django 4.2.3 on 2023-12-23 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogcomment',
        ),
    ]

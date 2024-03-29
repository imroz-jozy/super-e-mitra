# Generated by Django 5.0 on 2024-01-17 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formfill', '0005_remove_userform_pdf_files_alter_userform_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userform',
            name='photos',
        ),
        migrations.CreateModel(
            name='UserformImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='userform_photos/')),
                ('userform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formfill.userform')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-12-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
                ('TimeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]

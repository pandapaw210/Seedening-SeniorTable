# Generated by Django 4.1.4 on 2023-01-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]

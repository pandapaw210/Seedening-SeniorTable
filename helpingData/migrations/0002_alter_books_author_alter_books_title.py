# Generated by Django 4.1.4 on 2023-01-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpingData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
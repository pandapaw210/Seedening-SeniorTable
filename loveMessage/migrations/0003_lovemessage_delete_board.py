# Generated by Django 4.1.4 on 2023-01-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveMessage', '0002_board_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='loveMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('contents', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0016_remove_userstatistic_runes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='difficulty',
            field=models.IntegerField(default=1, verbose_name='Сложность'),
        ),
    ]

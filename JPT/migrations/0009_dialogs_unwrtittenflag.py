# Generated by Django 3.1.7 on 2021-06-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPT', '0008_auto_20210616_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialogs',
            name='UnWrtittenFlag',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

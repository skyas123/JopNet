# Generated by Django 3.1.7 on 2021-05-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPT', '0002_auto_20210516_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='Status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
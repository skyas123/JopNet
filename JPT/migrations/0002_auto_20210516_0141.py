# Generated by Django 3.1.7 on 2021-05-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPT', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='Status',
        ),
        migrations.AddField(
            model_name='friends',
            name='pair',
            field=models.ManyToManyField(to='JPT.Persons'),
        ),
    ]

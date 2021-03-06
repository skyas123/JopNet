# Generated by Django 3.1.7 on 2021-03-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='ava',
            field=models.ManyToManyField(blank=True, null=True, to='JPT.Media'),
        ),
        migrations.AlterField(
            model_name='persons',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_persons_friends_+', to='JPT.Persons'),
        ),
    ]

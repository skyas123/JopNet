# Generated by Django 3.1.7 on 2021-03-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subphoto', models.ManyToManyField(to='JPT.Media')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('second_name', models.CharField(default='', max_length=30)),
                ('date_of_appearence', models.DateField()),
                ('size', models.IntegerField(blank=True, default=0, null=True)),
                ('login', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('ava', models.ManyToManyField(to='JPT.Media')),
                ('friends', models.ManyToManyField(related_name='_persons_friends_+', to='JPT.Persons')),
            ],
        ),
    ]

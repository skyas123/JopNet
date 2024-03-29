# Generated by Django 3.1.7 on 2021-05-15 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appearence', models.DateTimeField(auto_now_add=True)),
                ('dialogname', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appearence', models.DateField(null=True)),
                ('size', models.IntegerField(blank=True, default=0, null=True)),
                ('ava', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JPT.media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JPT.persons')),
                ('subphoto', models.ManyToManyField(to='JPT.Media')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appearence', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('atachment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JPT.dialogs')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JPT.persons')),
                ('subphoto', models.ManyToManyField(to='JPT.Media')),
            ],
        ),
        migrations.AddField(
            model_name='dialogs',
            name='dialogPfoto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JPT.media'),
        ),
        migrations.AddField(
            model_name='dialogs',
            name='listOfMembers',
            field=models.ManyToManyField(to='JPT.Persons'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JPT', '0004_friends_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='ava',
            field=models.ForeignKey(blank=True, default='settings.MEDIA_ROOT/media/DSCN4415.jpg', null=True, on_delete=django.db.models.deletion.CASCADE, to='JPT.media'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-07-09 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20210620_1308'),
        ('climax_tracker', '0006_alter_climaxprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climaxprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='climax_profile', to='stats.profile'),
        ),
    ]

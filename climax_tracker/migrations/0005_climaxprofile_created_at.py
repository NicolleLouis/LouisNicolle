# Generated by Django 3.2.4 on 2021-07-07 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('climax_tracker', '0004_bet_motive'),
    ]

    operations = [
        migrations.AddField(
            model_name='climaxprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
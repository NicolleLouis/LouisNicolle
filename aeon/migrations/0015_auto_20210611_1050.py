# Generated by Django 3.2.4 on 2021-06-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeon', '0014_auto_20210611_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='breach_number',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='can_destroy_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('GEM', 'Gem'), ('RELIC', 'Relic'), ('SPELL', 'Spell')], default='UNKNOWN', max_length=7),
        ),
        migrations.AddField(
            model_name='card',
            name='damage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='ether_gain',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='ether_maximum_gain',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='maximum_damage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='overtime_effect',
            field=models.BooleanField(default=False),
        ),
    ]

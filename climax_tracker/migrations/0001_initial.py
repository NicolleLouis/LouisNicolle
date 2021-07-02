# Generated by Django 3.2.4 on 2021-07-02 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stats', '0002_auto_20210620_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClimaxProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('climax_eaten', models.IntegerField(blank=True, default=0, null=True)),
                ('climax_account', models.IntegerField(blank=True, default=0, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stats.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('climax_amount', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet_loser', to='climax_tracker.climaxprofile')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet_winner', to='climax_tracker.climaxprofile')),
            ],
        ),
    ]

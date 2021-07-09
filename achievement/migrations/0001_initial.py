# Generated by Django 3.2.4 on 2021-07-09 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stats', '0002_auto_20210620_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('key', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AchievementLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.IntegerField(default=1)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='achievement.achievement')),
            ],
        ),
        migrations.CreateModel(
            name='AchievementGranted',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('granted_at', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='achievement.achievement')),
                ('achievement_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='achievement.achievementlevel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stats.profile')),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeon', '0019_game_number_of_mage'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_difficulty',
            field=models.CharField(choices=[('STANDARD', 'Standard'), ('HARD', 'Hard')], default='STANDARD', max_length=8),
        ),
    ]

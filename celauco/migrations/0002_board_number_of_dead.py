# Generated by Django 3.2.4 on 2021-09-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celauco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='number_of_dead',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
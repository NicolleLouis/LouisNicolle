# Generated by Django 3.1.7 on 2021-06-09 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aeon', '0002_auto_20210609_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('french_name', models.CharField(blank=True, max_length=50, null=True)),
                ('english_name', models.CharField(blank=True, max_length=50, null=True)),
                ('ether_cost', models.IntegerField(blank=True, null=True)),
                ('is_self_destroyable', models.BooleanField(default=False)),
                ('has_utility', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aeon.card')),
                ('ether_win', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Gem',
                'verbose_name_plural': 'Gems',
            },
            bases=('aeon.card',),
        ),
        migrations.CreateModel(
            name='Relic',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aeon.card')),
                ('damage', models.IntegerField(blank=True, null=True)),
                ('ether_win', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Relic',
                'verbose_name_plural': 'Relics',
            },
            bases=('aeon.card',),
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aeon.card')),
                ('damage', models.IntegerField(blank=True, null=True)),
                ('breach_number', models.IntegerField(blank=True, default=1, null=True)),
            ],
            options={
                'verbose_name': 'Spell',
                'verbose_name_plural': 'Spells',
            },
            bases=('aeon.card',),
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.UniqueConstraint(fields=('french_name',), name='unique_card_french_name'),
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.UniqueConstraint(fields=('english_name',), name='unique_card_english_name'),
        ),
    ]
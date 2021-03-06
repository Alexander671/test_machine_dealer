# Generated by Django 4.0.4 on 2022-04-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('official', models.BooleanField()),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Dealer',
                'verbose_name_plural': 'Dealers',
            },
        ),
    ]

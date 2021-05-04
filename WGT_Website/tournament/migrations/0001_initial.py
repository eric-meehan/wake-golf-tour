# Generated by Django 3.1.7 on 2021-03-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('round_id', models.AutoField(primary_key=True, serialize=False)),
                ('round_day', models.TextField()),
            ],
            options={
                'db_table': 'Round',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tourn_id', models.AutoField(primary_key=True, serialize=False)),
                ('tourn_name', models.TextField()),
                ('tourn_start_date', models.DateField()),
                ('tourn_num_rounds', models.IntegerField()),
                ('tourn_num_golfers', models.IntegerField()),
            ],
            options={
                'db_table': 'Tournament',
                'managed': False,
            },
        ),
    ]

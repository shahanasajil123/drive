# Generated by Django 3.2.24 on 2024-04-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secondarynumber',
            fields=[
                ('secondary_number_id', models.AutoField(db_column='secondary number_id', primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'secondarynumber',
                'managed': False,
            },
        ),
    ]
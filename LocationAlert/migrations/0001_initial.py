# Generated by Django 3.2.24 on 2024-04-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locationalert',
            fields=[
                ('location_alert_id', models.AutoField(db_column='location alert_id', primary_key=True, serialize=False)),
                ('alert', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'locationalert',
                'managed': False,
            },
        ),
    ]

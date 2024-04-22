# Generated by Django 3.2.24 on 2024-04-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('hospital_name', models.CharField(db_column='hospital name', max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('contact_number', models.IntegerField(db_column='contact number')),
            ],
            options={
                'db_table': 'hospital',
                'managed': False,
            },
        ),
    ]

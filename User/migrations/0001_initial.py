# Generated by Django 3.2.24 on 2024-04-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=45)),
                ('user_address', models.CharField(max_length=45)),
                ('user_number', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
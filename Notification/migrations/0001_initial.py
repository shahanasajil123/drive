# Generated by Django 3.2.24 on 2024-04-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'notification',
                'managed': False,
            },
        ),
    ]

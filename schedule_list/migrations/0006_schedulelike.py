# Generated by Django 5.0.1 on 2024-01-06 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_list', '0005_remove_schedule_guest_id'),
        ('user', '0002_rename_user_name_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_id', models.ForeignKey(db_column='schedule_id', on_delete=django.db.models.deletion.CASCADE, to='schedule_list.schedule')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]

# Generated by Django 3.1.11 on 2021-05-17 13:21

import core.models.image_models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('envs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.image_models.content_file_name)),
                ('public_id', models.CharField(db_index=True, editable=False, max_length=15, unique=True, verbose_name='public_id')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
                ('title', models.CharField(max_length=500, verbose_name='name')),
                ('language', models.ForeignKey(limit_choices_to={'envs_type_name': 'languages'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='languages', to='envs.attributes')),
                ('tree_channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tree_channels', to='channels.channel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

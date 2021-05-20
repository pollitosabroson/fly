# Generated by Django 3.1.11 on 2021-05-20 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envs', '0001_initial'),
        ('contents', '0002_auto_20210519_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='kind',
            field=models.ForeignKey(limit_choices_to={'envs_type__name': 'content'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='kinds', to='envs.attributes'),
        ),
    ]

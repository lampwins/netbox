# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0003_unicode_literals'),
        ('dcim', '0050_interface_vlan_tagging'),
    ]

    operations = [
        migrations.AddField(
            model_name='rackreservation',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rackreservations', to='tenancy.Tenant'),
        ),
    ]

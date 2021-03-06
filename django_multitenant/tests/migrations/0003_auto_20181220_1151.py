# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_distribute'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE tests_tenantnotidmodel DROP CONSTRAINT tests_tenantnotidmodel_pkey CASCADE;"),
        migrations.RunSQL("ALTER TABLE tests_somerelatedmodel DROP CONSTRAINT tests_somerelatedmodel_pkey CASCADE;"),

        migrations.RunSQL("SELECT create_distributed_table('tests_tenantnotidmodel', 'tenant_column');"),
        migrations.RunSQL("SELECT create_distributed_table('tests_somerelatedmodel', 'related_tenant_id');"),

        migrations.RunSQL("ALTER TABLE tests_somerelatedmodel ADD CONSTRAINT tests_somerelatedmodel_pkey PRIMARY KEY (related_tenant_id, id);"),
        migrations.RunSQL("ALTER TABLE tests_tenantnotidmodel ADD CONSTRAINT tests_tenantnotidmodel_pkey PRIMARY KEY (tenant_column);")
    ]

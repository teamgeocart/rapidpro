# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-16 17:05
from __future__ import unicode_literals

from django.db import migrations

SQL = """
CREATE INDEX locations_adminboundary_name on locations_adminboundary(upper("name"));

CREATE INDEX locations_boundaryalias_name on locations_boundaryalias(upper("name"));
"""


class Migration(migrations.Migration):

    dependencies = [("locations", "0002_auto_20180716_1622")]

    operations = [migrations.RunSQL(SQL)]

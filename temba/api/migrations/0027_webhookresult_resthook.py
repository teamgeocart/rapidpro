# Generated by Django 2.1.5 on 2019-02-08 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0026_auto_20190129_2156")]

    operations = [
        migrations.AddField(
            model_name="webhookresult",
            name="resthook",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="api.Resthook"),
        )
    ]

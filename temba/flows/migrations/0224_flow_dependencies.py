# Generated by Django 2.2.4 on 2020-02-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("templates", "0004_initial"), ("flows", "0223_convert_flow_metadata")]

    operations = [
        migrations.AddField(
            model_name="flow",
            name="template_dependencies",
            field=models.ManyToManyField(related_name="dependent_flows", to="templates.Template"),
        ),
        migrations.AlterField(
            model_name="flow",
            name="field_dependencies",
            field=models.ManyToManyField(related_name="dependent_flows", to="contacts.ContactField"),
        ),
        migrations.AlterField(
            model_name="flow",
            name="flow_dependencies",
            field=models.ManyToManyField(related_name="dependent_flows", to="flows.Flow"),
        ),
        migrations.AlterField(
            model_name="flow",
            name="group_dependencies",
            field=models.ManyToManyField(related_name="dependent_flows", to="contacts.ContactGroup"),
        ),
    ]

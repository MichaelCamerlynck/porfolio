# Generated by Django 4.1 on 2023-02-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_project_challenges_project_results_project_roles_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="img",
            name="position",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 4.1 on 2023-02-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_project_roles_list"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="show",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

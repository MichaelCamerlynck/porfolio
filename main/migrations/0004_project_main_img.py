# Generated by Django 4.1 on 2023-02-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_project_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="main_img",
            field=models.CharField(default="imgs/Artificial_Img_1.png", max_length=100),
            preserve_default=False,
        ),
    ]
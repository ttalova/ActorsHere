# Generated by Django 4.2 on 2023-05-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_app", "0007_alter_actorprofile_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actorprofile",
            name="rating",
            field=models.PositiveIntegerField(default=5),
        ),
    ]

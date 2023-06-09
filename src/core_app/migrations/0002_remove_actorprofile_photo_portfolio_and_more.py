# Generated by Django 4.2 on 2023-04-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="actorprofile",
            name="photo_portfolio",
        ),
        migrations.RemoveField(
            model_name="casting",
            name="additional_photo",
        ),
        migrations.AlterField(
            model_name="actorprofile",
            name="clothing_size",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="actorprofile",
            name="height",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="actorprofile",
            name="main_photo",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="actorprofile",
            name="rating",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="actorprofile",
            name="shoe_size",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="actorprofile",
            name="weight",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="casting",
            name="photo",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="employerprofile",
            name="photo",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="employerprofile",
            name="rating",
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name="AdditionalPhoto",
        ),
    ]

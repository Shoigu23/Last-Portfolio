# Generated by Django 4.2 on 2023-04-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="main.tag", verbose_name="Направление"),
        ),
    ]

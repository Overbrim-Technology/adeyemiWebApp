# Generated by Django 5.2 on 2025-04-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]

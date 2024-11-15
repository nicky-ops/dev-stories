# Generated by Django 5.1.2 on 2024-11-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0003_user_avatar"),
        ("post_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="posts_liked",
            field=models.ManyToManyField(related_name="liked_by", to="post_app.post"),
        ),
    ]
# Generated by Django 4.1.5 on 2023-05-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oauth_app", "0004_alter_userinfo_age_alter_userinfo_classes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="role",
            field=models.CharField(
                choices=[("student", "student"), ("school_admin", "school_admin")],
                max_length=20,
                null=True,
            ),
        ),
    ]

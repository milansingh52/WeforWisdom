# Generated by Django 4.2.4 on 2023-10-07 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_rename_tut_id_tutor_rating_tut_id1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tutor_rating",
            old_name="tut_id1",
            new_name="tut_id",
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-24 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_profile", models.ImageField(upload_to="media/author")),
                ("name", models.CharField(max_length=100, null=True)),
                ("about_author", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "feature_photo",
                    models.ImageField(null=True, upload_to="feature_img"),
                ),
                ("feature_video", models.CharField(max_length=300, null=True)),
                ("title", models.CharField(max_length=500)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("category", models.CharField(max_length=200, null=True)),
                ("description", models.TextField()),
                ("price", models.IntegerField(null=True)),
                ("validity_days", models.IntegerField(null=True)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Private_Tutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=10)),
                ("teaching_fee", models.CharField(max_length=20)),
                ("gender", models.CharField(max_length=10)),
                ("live_area", models.CharField(max_length=20)),
                ("dob", models.CharField(max_length=10)),
                ("study_status", models.CharField(max_length=50)),
                ("teaching_exp", models.CharField(max_length=50)),
                ("teaching_area", models.CharField(max_length=50)),
                ("teaching_category", models.CharField(max_length=50)),
                ("teaching_sub", models.CharField(max_length=50)),
                ("about_your_self", models.TextField()),
                ("demo_video", models.FileField(upload_to="private_tutor/video")),
                ("tutor_photo", models.ImageField(upload_to="tutor_img/")),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("serial_number", models.IntegerField(null=True)),
                ("thumbnail", models.ImageField(upload_to="thumbnails")),
                ("title", models.CharField(max_length=100)),
                ("youtube_id", models.CharField(max_length=200)),
                ("time_duration", models.IntegerField(null=True)),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.course",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.lesson"
                    ),
                ),
            ],
        ),
    ]

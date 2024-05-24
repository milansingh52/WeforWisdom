from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
# Create your models here.

# Login


# class CustomUser(AbstractUser):
#     USER = (
#         (1, 'Private_Tutor'),
#         (2, 'Course_Tutor'),
#         (3, 'Student')
#     )
#     user_type = models.CharField(choices=USER, max_length=50, default=1)
#     profile_pic = models.ImageField(upload_to='profile_pic')

tutor_id_to_assign = 1  # The ID of the desired Private_Tutor instance


class Author(models.Model):
    author_profile = models.ImageField(upload_to="media/author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    feature_photo = models.ImageField(upload_to='feature_img', null=True)
    feature_video = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.TextField()
    price = models.IntegerField(null=True)
    validity_days = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to="thumbnails")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=200)
    time_duration = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Private_Tutor(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    teaching_fee = models.CharField(max_length=20)

    gender = models.CharField(max_length=10)
    live_area = models.CharField(max_length=20)
    dob = models.CharField(max_length=10)
    study_status = models.CharField(max_length=50)
    teaching_exp = models.CharField(max_length=50)
    teaching_area = models.CharField(max_length=50)

    teaching_category = models.CharField(max_length=50)
    teaching_sub = models.CharField(max_length=50)

    about_your_self = models.TextField()

    demo_video = models.FileField(upload_to="private_tutor/video")

    tutor_photo = models.ImageField(upload_to="tutor_img/")
    # tutor_photo = models.URLField()

    def __str__(self):
        return self.email


class tutor_rating(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    rating_value = models.IntegerField(null=True)
    tut_id = models.IntegerField(null=True)  # Allow null values
    # tutor = models.ForeignKey(Private_Tutor, on_delete=models.CASCADE, default=None)


class Student(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

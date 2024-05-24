from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


class lesson_TabularInline(admin.TabularInline):
    model = Lesson


class video_TabularInline(admin.TabularInline):
    model = Video


class course_admin(admin.ModelAdmin):
    inlines = (lesson_TabularInline, video_TabularInline)


# admin.site.register(CustomUser, UserModel)


admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Private_Tutor)
admin.site.register(tutor_rating)
admin.site.register(Student)

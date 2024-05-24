"""
URL configuration for WeForWisdom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views, tutor_views, course_views, user_login

urlpatterns = [
    # General
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('about/', views.ABOUT, name='about'),
    path('', views.INDEX, name='index'),

    path('signup/', views.SIGNUP, name="signup"),
    path('login/', views.LOGIN, name="login"),
    path('logout/', views.LOGOUT, name="logout"),
    path('search/', views.SEARCH_COURSE, name="search_course"),
    path('test/', views.TEST, name="test"),

    # Payment
    path('payment/<int:price>', views.PAYMENT, name="payment"),
    path('payment-login/<int:price>', views.PAYMENT_LOGIN, name="payment_login"),

    # Student
    path('student-login/', views.STUDENT_LOGIN, name="student_login"),
    path('student-signup/', views.STUDENT_SIGNUP, name="student_signup"),

    # Tutor Urls
    path('tutor-home/', tutor_views.TUTOR_HOME, name='tutor_home'),
    path('tutor-list/', tutor_views.TUTOR_LIST, name='tutor_list'),
    path('tutor-details/<int:id>', tutor_views.TUTOR_DETAIL, name='tutor_detail'),
    path('become-a-tutor/', tutor_views.BECOME_A_TUTOR, name='become_a_tutor'),
    path('tutor-dashboard/', tutor_views.TUTOR_DASHBOARD, name='tutor_dashboard'),


    # Course Urls
    path('course-home/', course_views.COURSE_HOME, name="course_home"),
    path('course-detail/<int:courseid>',
         course_views.COURSE_DETAIL, name="course_detail"),
    path('course-view/<youtube_id>',
         course_views.COURSE_VIEW, name="course_view"),
    path('recommended-courses', course_views.RECOMMENDED_COURSE,
         name="recommended_courses"),

    # Course Selling Tutor
    path('dashboard-home/', tutor_views.DASHBOARD_HOME, name='dashboard_home'),
    path('dashboard-author/', tutor_views.DASHBOARD_AUTHOR, name='dashboard_author'),
    path('dashboard-course/', tutor_views.DASHBOARD_COURSE, name='dashboard_course'),
    path('dashboard-lesson/', tutor_views.DASHBOARD_LESSON, name='dashboard_lesson'),
    path('dashboard-video/', tutor_views.DASHBOARD_VIDEO, name='dashboard_video'),
    path('dashboard-profile/', tutor_views.DASHBOARD_PROFILE,
         name='dashboard_profile'),

    path('manage-author/', tutor_views.MANAGE_AUTHOR, name='manage_author'),
    path('manage-author2/<int:id>',
         tutor_views.MANAGE_AUTHOR2, name='manage_author2'),
    path('delete-author/<int:id>', tutor_views.DELETE_AUTHOR, name='delete_author'),

    path('manage-course/', tutor_views.MANAGE_COURSE, name='manage_course'),
    path('manage-course2/<int:id>',
         tutor_views.MANAGE_COURSE2, name='manage_course2'),
    path('delete-course/<int:id>', tutor_views.DELECT_COURSE, name='delete_course'),


    path('manage-lesson/', tutor_views.MANAGE_LESSON, name='manage_lesson'),
    path('manage-lesson2/<int:id>',
         tutor_views.MANAGE_LESSON2, name='manage_lesson2'),
    path('delete-lesson/<int:id>', tutor_views.DELETE_LESSON, name='delete_lesson'),


    path('manage-video/', tutor_views.MANAGE_VIDEO, name='manage_video'),
    path('manage-video2/<int:id>', tutor_views.MANAGE_VIDEO2, name='manage_video2'),
    path('delete-video/<int:id>', tutor_views.DELETE_VIDEO, name='delete_video'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

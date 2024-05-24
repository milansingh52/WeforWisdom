from django.shortcuts import render, redirect, get_object_or_404, redirect
from app.models import *
from django.db.models import Q
from django.contrib.auth.models import User


def TUTOR_HOME(request):
    return render(request, 'tutor/tutor_home.html')


def TUTOR_LIST(request):
    if request.method == 'POST':
        # category = request.POST.get('category')

        category_value = request.POST.get('category_value')
        subject = request.POST.get('subject')
        location = request.POST.get('location')

        if location:
            tutors = Private_Tutor.objects.filter(
                Q(teaching_category=category_value) & Q(teaching_sub=subject) & Q(live_area=location))
        else:
            tutors = Private_Tutor.objects.filter(
                Q(teaching_category=category_value) & Q(teaching_sub=subject))
            print(tutors)

    context = {
        'tutors': tutors,
        'category_value': category_value,
        'subject': subject,
    }
    return render(request, 'tutor/tutor_list.html', context)


def TUTOR_DETAIL(request, id):
    tutor = Private_Tutor.objects.filter(id=id)
    rating = tutor_rating.objects.filter(tut_id=id)

    context = {
        'tutors': tutor,
        'rating': rating
    }

    # for rating
    if request.method == 'POST':
        name = request.POST.get('name')
        r_comment = request.POST.get('r_comment')
        r_value = request.POST.get('r_value')
        rating = tutor_rating()

        rating.name = name
        rating.comment = r_comment
        rating.rating_value = r_value
        rating.tut_id = id

        rating.save()

    return render(request, 'tutor/tutor_details.html', context)


def BECOME_A_TUTOR(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, "tutor/become_a_tutor.html", {})

            except User.DoesNotExist:
                # section 1 data
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                phone = request.POST.get('phone')
                teaching_fee = request.POST.get('fee')

                # print(name, email, phone, password, cpassword, teaching_fee)

                # section 2 data
                gender = request.POST.get('gender')
                live_area = request.POST.get('live_area')
                dob = request.POST.get('dob')
                study_status = request.POST.get('study_status')
                teaching_exp = request.POST.get('teaching_exp')
                teaching_area = request.POST.get('teaching_area')
                # print(gender, live_area, dob, study_status,teaching_exp, teaching_area)

                # section 3 data
                teaching_cat = request.POST.get('category')
                teaching_sub = request.POST.get('subject')

                # section 4 data
                about_your_self = request.POST.get('about_your_self')

                # section 5
                video_file = request.FILES['video']

                # section 5
                image_file = request.FILES['image']

                # print(teaching_cat, teaching_sub,about_your_self,  tutor_video, tutor_photo)

                tutor = Private_Tutor()

                # set data
                tutor.name = name
                tutor.email = email
                tutor.password = password
                tutor.phone = phone
                tutor.teaching_fee = teaching_fee

                tutor.gender = gender
                tutor.live_area = live_area
                tutor.dob = dob
                tutor.study_status = study_status
                tutor.teaching_exp = teaching_exp
                tutor.teaching_area = teaching_area

                tutor.teaching_category = teaching_cat
                tutor.teaching_sub = teaching_sub

                tutor.about_your_self = about_your_self

                tutor.demo_video = video_file
                tutor.tutor_photo = image_file

                # save data
                tutor.save()

                user = User.objects.create_user(
                    username=email, password=password)

                return render(request, "tutor/become_a_tutor.html", {})
        else:
            return render(request, 'tutor/become_a_tutor.html', {'error': "Passwords Don't Match"})

    else:
        return render(request, "tutor/become_a_tutor.html", {})


def TUTOR_DASHBOARD(request):
    return render(request, "course_selling_tutor/home.html")


def DASHBOARD_AUTHOR(request):
    authors = Author.objects.all()
    return render(request, 'course_selling_tutor/author.html', {'authors': authors})


def DASHBOARD_COURSE(request):
    courses = Course.objects.all()
    return render(request, 'course_selling_tutor/course.html', {'courses': courses})


def DASHBOARD_LESSON(request):
    lessons = Lesson.objects.all()
    return render(request, 'course_selling_tutor/lesson.html', {'lessons': lessons})


def DASHBOARD_VIDEO(request):
    videos = Video.objects.all()
    return render(request, 'course_selling_tutor/video.html', {'videos': videos})


def DASHBOARD_HOME(request):
    return render(request, 'course_selling_tutor/home.html')


def DASHBOARD_PROFILE(request):
    return render(request, 'course_selling_tutor/profile.html')


def MANAGE_AUTHOR(request):
    if request.method == 'POST':
        author_img = request.FILES['image']
        name = request.POST.get('name')
        about = request.POST.get('about')

        author = Author()
        author.author_profile = author_img
        author.name = name
        author.about_author = about

        author.save()
        authors = Author.objects.all()
        return render(request, 'course_selling_tutor/author.html', {'authors': authors})

    return render(request, 'course_selling_tutor/manage/manage_author.html')


def MANAGE_AUTHOR2(request, id=None):
    if request.method == 'POST':
        name = request.POST.get('name')
        about = request.POST.get('about')

        if id:
            author = get_object_or_404(Author, id=id)
            author.name = name
            author.about_author = about
            if 'image' in request.FILES:
                author.author_profile = request.FILES['image']
            author.save()
            authors = Author.objects.all()
            return render(request, 'course_selling_tutor/author.html', {'authors': authors})
        else:
            author_img = request.FILES.get('image')
            author = Author(name=name, about_author=about,
                            author_profile=author_img)
            author.save()
            authors = Author.objects.all()
            return render(request, 'course_selling_tutor/author.html', {'authors': authors})

    if id:
        aut = get_object_or_404(Author, id=id)
    else:
        aut = None

    return render(request, 'course_selling_tutor/manage/manage_author2.html', {'author': aut})


def DELETE_AUTHOR(request, id):
    print(id)
    aut = Author.objects.get(id=id)
    aut.delete()

    authors = Author.objects.all()
    return render(request, 'course_selling_tutor/author.html', {'authors': authors})


def MANAGE_COURSE(request):
    if request.method == 'POST':
        feature_video = request.POST.get('fvideo')
        title = request.POST.get('title')
        author_name = request.POST.get('author')  # Retrieve the author's name
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        validity_days = request.POST.get('vdays')

        # Retrieve the Author instance based on the provided name
        author = Author.objects.get(name=author_name)

        # Check if an image has been provided
        if 'image' in request.FILES and request.FILES['image']:
            feature_img = request.FILES['image']
        else:
            # Handle the case where no image is provided
            # You can set a default image or handle it as needed
            feature_img = None  # Set a default image or None, depending on your requirements

        course = Course()
        course.feature_photo = feature_img
        course.feature_video = feature_video
        course.title = title
        course.author = author  # Assign the Author instance
        course.category = category
        course.description = description
        course.price = price
        course.validity_days = validity_days

        course.save()
        courses = Course.objects.all()
        return render(request, 'course_selling_tutor/course.html', {'courses': courses})

    authors = Author.objects.all()
    return render(request, 'course_selling_tutor/manage/manage_course.html', {'authors': authors})


def MANAGE_COURSE2(request, id=None):
    print(id)
    if request.method == 'POST':
        feature_video = request.POST.get('fvideo')
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        validity_days = request.POST.get('vdays')

        author = Author.objects.get(name=author_name)

        coursee = get_object_or_404(Course, id=id)
        print(coursee)
        coursee.feature_video = feature_video
        coursee.title = title
        coursee.author = author  # Assign the Author instance
        coursee.category = category
        coursee.description = description
        coursee.price = price
        coursee.validity_days = validity_days

        if 'image' in request.FILES and request.FILES['image']:
            coursee.feature_photo = request.FILES['image']

        coursee.save()
        courses = Course.objects.all()
        return render(request, 'course_selling_tutor/course.html', {'courses': courses})

    authors = Author.objects.all()
    if id:
        course = get_object_or_404(Course, id=id)
    else:
        course = None

    return render(request, 'course_selling_tutor/manage/manage_course2.html', {'course': course, 'authors': authors})


def DELECT_COURSE(request, id):
    c = Course.objects.get(id=id)
    c.delete()

    courses = Course.objects.all()
    return render(request, 'course_selling_tutor/course.html', {'courses': courses})


def MANAGE_LESSON(request):
    if request.method == 'POST':
        course_title = request.POST.get('course')
        name = request.POST.get('name')

        course = Course.objects.get(title=course_title)

        lesson = Lesson()
        lesson.course = course
        lesson.name = name

        lesson.save()

        lessons = Lesson.objects.all()
        return render(request, 'course_selling_tutor/lesson.html', {'lessons': lessons})

    courses = Course.objects.all()
    return render(request, 'course_selling_tutor/manage/manage_lesson.html', {'courses': courses})


def MANAGE_LESSON2(request, id):
    if request.method == 'POST':
        course_title = request.POST.get('course')
        name = request.POST.get('name')

        course = Course.objects.get(title=course_title)

        lesson = get_object_or_404(Lesson, id=id)

        lesson.course = course
        lesson.name = name
        lesson.save()

        lessons = Lesson.objects.all()
        return render(request, 'course_selling_tutor/lesson.html', {'lessons': lessons})
    if id:
        lesson = get_object_or_404(Lesson, id=id)
    else:
        lesson = None
    return render(request, 'course_selling_tutor/manage/manage_lesson2.html', {'lesson': lesson})


def DELETE_LESSON(request, id):
    l = Lesson.objects.get(id=id)
    l.delete()

    lessons = Lesson.objects.all()
    return render(request, 'course_selling_tutor/lesson.html', {'lessons': lessons})


def MANAGE_VIDEO(request):

    if request.method == 'POST':
        video = Video()

        video.serial_number = request.POST.get('sn')
        course = Course.objects.get(title=request.POST.get('course'))
        video.course = course

        lesson = Lesson.objects.get(name=request.POST.get('lesson'))
        video.lesson = lesson

        video.title = request.POST.get('title')
        video.youtube_id = request.POST.get('youtube_id')
        video.time_duration = request.POST.get('time_duration')

        if 'image' in request.FILES and request.FILES['image']:
            video.thumbnail = request.FILES['image']

        video.save()
        videos = Video.objects.all()
        return render(request, 'course_selling_tutor/video.html', {'videos': videos})

    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    return render(request, 'course_selling_tutor/manage/manage_video.html', {'courses': courses, 'lessons': lessons})


def MANAGE_VIDEO2(request, id):
    if request.method == 'POST':

        video = get_object_or_404(Video, id=id)

        video.serial_number = request.POST.get('sn')
        course = Course.objects.get(title=request.POST.get('course'))
        video.course = course

        lesson = Lesson.objects.get(name=request.POST.get('lesson'))
        video.lesson = lesson

        video.title = request.POST.get('title')
        video.youtube_id = request.POST.get('youtube_id')
        video.time_duration = request.POST.get('time_duration')

        if 'image' in request.FILES and request.FILES['image']:
            video.thumbnail = request.FILES['image']

        video.save()
        videos = Video.objects.all()
        return render(request, 'course_selling_tutor/video.html', {'videos': videos})
    if id:
        video = get_object_or_404(Video, id=id)
    else:
        video = None
    return render(request, 'course_selling_tutor/manage/manage_video2.html', {'video': video})


def DELETE_VIDEO(request, id):
    v = Video.objects.get(id=id)
    v.delete()

    videos = Video.objects.all()
    return render(request, 'course_selling_tutor/video.html', {'videos': videos})

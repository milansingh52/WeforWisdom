from django.shortcuts import render, redirect, HttpResponse
from app.models import *
from django.contrib.auth.models import User
from django.contrib import auth
# base file path


def BASE(request):
    return render(request, 'Main/base.html')


def TEST(request):
    return render(request, 'Main/test.html')


def INDEX(request):
    # course = Course.objects.all().order_by('-id')[1:9]
    course = Course.objects.all()
    context = {
        'courses': course,
    }
    return render(request, 'Main/index.html', context)


def ABOUT(request):
    return render(request, 'Main/about.html')


def LOGIN(request):
    if request.method == "POST":
        # check if a user exists
        # with the username and password
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("/tutor-dashboard/")
            # return HttpResponse("Welcome")
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid Username and Password'})

    else:
        return render(request, 'registration/login.html')


def LOGOUT(request):
    auth.logout(request)
    return redirect("/login/")


def SIGNUP(request):
    if request.method == 'POST':
        # create a user
        if request.POST['password'] == request.POST['cpassword']:
            # both the passwords matched
            # now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'registration/signup.html', {'error': "Email has already been taken"})

            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['email'], password=request.POST['password'], first_name=request.POST['name'])
            return redirect("/login/")
        else:
            return render(request, 'registration/signup.html', {'error': "Passwords Don't Match"})

    else:
        return render(request, 'registration/signup.html')


def PAYMENT(request, price):
    if request.method == 'POST':
        return render(request, 'payment/esewa_form.html', {'price': price})
    return render(request, 'payment/esewa_form.html',)


def PAYMENT_LOGIN(request, price):
    # 9806800002
    if request.method == 'POST':
        esewa_id1 = request.POST.get('eswea_id')
        password1 = request.POST.get('password')

        if esewa_id1 == '9806800002' and password1 == '12345':
            if price <= 900:
                return render(request, 'payment/payment_success.html')
            else:
                return render(request, 'payment/payment_failed.html')
        else:
            print('no hello')
    return render(request, 'payment/payment_success.html')


def STUDENT_LOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        students = Student.objects.all()

        for student in students:
            if student.email == email and student.password == password:
                # Store student ID in the session
                request.session['student_id'] = student.id
                request.session['product_id'] = 123
                # Redirect to the student dashboard page
                return redirect('/payment/')

        error_message = "Invalid email or password. Please try again."
        return render(request, 'student/login.html', {'error_message': error_message})

    return render(request, 'login.html')


def STUDENT_SIGNUP(request):
    if request.method == 'POST':
        stu = Student()
        stu.email = request.POST.get('email')
        stu.name = request.POST.get('name')
        stu.password = request.POST.get('password')
        stu.phone = request.POST.get('phone')

        stu.save()
        return render(request, 'student/login.html')

    return render(request, 'student/signup.html')


def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains=query)
    context = {
        'courses': course,
    }
    return render(request, 'search/search.html', context)

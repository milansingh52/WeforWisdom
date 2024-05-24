from django.shortcuts import render, redirect
from app.models import *
import pickle
import pandas as pd

# Course Home


def COURSE_HOME(request):
    course = Course.objects.all()
    course_title = df['course_title']
    context = {
        'courses': course,
        'course_title': course_title,
    }
    if request.method == 'POST':
        selected_value = request.POST.get('course')
        # print(selected_value)
        recommended_courses = recommend_course(selected_value).values.tolist()
        # print(recommended_courses)
        return render(request, 'course/course_home.html', {'recommended_courses': recommended_courses, 'courses': course})

    return render(request, 'course/course_home.html', context)

# Recommended Course


def RECOMMENDED_COURSE(request):
    course = Course.objects.all()
    course_title = df['course_title']
    context = {
        'courses': course,
        'course_title': course_title,
    }
    if request.method == 'POST':
        selected_value = request.POST.get('course')
        recommended_courses = recommend_course(selected_value).values.tolist()

        context = {
            'recommended_courses': recommended_courses,
            'courses': course,  # Make sure 'course' is defined correctly
        }

        return render(request, 'course/recommended_courses.html', context)

    return render(request, 'course/recommended_courses.html', context)


def COURSE_DETAIL(request, courseid):
    course = Course.objects.filter(id=courseid)
    context = {
        'courses': course,
    }

    return render(request, 'course/course_detial.html', context)


def COURSE_VIEW(request, youtube_id):
    return render(request, 'course/course_view.html', {'youtube_id': youtube_id})


# for recommendation system
with open('static/model/course_list.pkl', 'rb') as course_file:
    df = pickle.load(course_file)

with open('static/model/similarity.pkl', 'rb') as similarity_file:
    cosine_sim_mat = pickle.load(similarity_file)


course_indices = dict(zip(df['course_title'], df.index))


def recommend_course(title, num_of_rec=10):
    idx = course_indices[title]
    scores = list(enumerate(cosine_sim_mat[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    selected_course_indices = [i[0] for i in sorted_scores[1:]]
    selected_course_scores = [i[1] for i in sorted_scores[1:]]
    result = df.iloc[selected_course_indices][['course_title', 'url', 'price',
                                               'num_subscribers', 'num_reviews', 'num_lectures', 'level', 'content_duration', 'subject']]

    rec_df = pd.DataFrame(result)
    rec_df['similarity_scores'] = selected_course_scores
    return rec_df.head(num_of_rec)

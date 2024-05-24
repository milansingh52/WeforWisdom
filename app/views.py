from django.shortcuts import render
import pickle

movies = pickle.load(open('static/movies_list.pkl', 'rb'))
similarity = pickle.load(open('static/similarity.pkl', 'rb'))

movies_list = movies['title'].values


def recommand(movie):
    index = movies[movies['title'] == movie].index[0]

    distance = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []

    for i in distance[0:5]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

# Create your views here.


def index(request):
    if request.method == "POST":
        selected_value = request.POST.get('movie')
        rec_movies = recommand(selected_value)

        return render(request, 'home.html', {'movies_list': movies_list, 'rec_movies': rec_movies})

    return render(request, 'home.html', {'movies_list': movies_list})

from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author' : 'Aditya',
        'title' : 'Blog Post 1',
        'content' : 'First post',
        'date_posted' : 'July 20, 2021' 
    },
    {
        'author' : 'AYushi',
        'title' : 'Blog Post 2',
        'content' : 'Second post',
        'date_posted' : 'July 21, 2021' 
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})
    
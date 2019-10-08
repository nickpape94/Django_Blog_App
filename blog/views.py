from django.shortcuts import render

posts = [
    {
        'author': 'Nick',
        'title': 'Blog post 1',
        'content': 'Blog post one',
        'date_posted': '08/10/2019'
    },
    {
        'author': 'James',
        'title': 'Blog post 2',
        'content': 'Blog post two',
        'date_posted': '18/10/2019'
    }


]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

# Create your views here.

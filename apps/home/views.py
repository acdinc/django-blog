from django.shortcuts import render


def home_view(request):

    template = 'home.html'
    context = {
        'isim': 'Ali',
        'nav_home': 'active',
    }

    return render(request, template, context)

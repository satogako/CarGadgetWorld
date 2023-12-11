from django.shortcuts import render


def index(request):
    '''
    Renders view for the homepag
    '''
    return render(request, "home/index.html")

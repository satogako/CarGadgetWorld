from django.shortcuts import render


def index(request):
    '''
    Renders view for the homepag
    '''
    return render(request, 'home/index.html')


def news_letter(request):
    '''
    Renders view for the newsletter page
    '''
    return render(request, 'home/newsletter.html')


def privacy_policy(request):
    '''
    Renders view for the privacy policy page
    '''
    return render(request, 'home/privacy_policy.html')

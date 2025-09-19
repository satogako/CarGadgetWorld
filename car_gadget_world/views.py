from django.shortcuts import render

# Temporary for creating an admin user
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin_user(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
        return HttpResponse("Admin created")
    return HttpResponse("Admin already exists")


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

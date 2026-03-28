from django.http import HttpResponse
from django.shortcuts import render,redirect

from .service.user_service import UserService


def welcome(request):
    return HttpResponse("<h1>Welcome to ch</h1>")
def user_signup(request):
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['email'] = request.POST.get('email')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
    return render(request, 'registration.html')

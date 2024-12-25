from urllib import response
from django.db import IntegrityError
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Projects, Profile, Tasks 
from .serializer import ProjectsSerializer,TaskViewSerializer,ProfileViewSerializer
from django.views.generic import TemplateView
from django.dispatch import receiver
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskViewSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileViewSerializer


class LoginRequired(LoginRequiredMixin):
    login_url = "/login/"




class Logout_view(View):
    def get(self, request):
        logout(request)
        return redirect('index')



class index(LoginRequired, View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)

class Login_view(View):
    template_name = "index.html"
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else: 
            return render(request, self.template_name, {'message': 'invalid name or password'})
        

class Register_view(View):

    template_name = "index.html"
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            profile = Profile.objects.all()
            user = User.objects.create_user(username, email, password)
            user.save()
            profile.create(user= user)
            

        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

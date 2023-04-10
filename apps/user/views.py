# Create your views here.
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login



class UserProfileView(UpdateView):
    model = User
    template_name = 'profil.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        return context
    


class CreateUserView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context =  super(CreateUserView, self).get_context_data(**kwargs)
        return context

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context
    def get_success_url(self):
        return reverse_lazy('home')

def logoutUser(request):
    logout(request)
    return redirect('login')



class EmailVerificationView(TemplateView):
    template_name = 'verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email = kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code = code)
        if email_verification.exists():
            user.is_confirm_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')



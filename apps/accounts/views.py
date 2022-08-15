from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages


from .forms import  RegisterForm
from .mixins import NotAuthenticatedMixin
# Create your views here.

class Login(NotAuthenticatedMixin, LoginView):
    template_name = "accounts/login.html"
    def get_success_url(self):
        return reverse_lazy('card:home')

class Register(NotAuthenticatedMixin, CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Information saved")
        return  redirect('card:home')
    def form_invalid(self, form):
        messages.error(self.request, "Invalid information")
        return redirect("accounts:login")

        
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('card:home')
    else:
        return redirect('accounts:login')
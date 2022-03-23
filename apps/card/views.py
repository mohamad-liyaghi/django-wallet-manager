from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from account.models import User
# Create your views here.
class Home(LoginRequiredMixin,ListView):
    template_name = "card/home.html"
    def get_queryset(self):
        return self.request.user.fund
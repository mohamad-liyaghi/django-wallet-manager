from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,FormView,ListView
from django.contrib import messages
from account.models import User
from card.models import Transaction
from .forms import CardForm
from account.forms import RegisterForm
# Create your views here.
class Home(LoginRequiredMixin,ListView):
    template_name = "card/home.html"
    def get_queryset(self):
        return self.request.user.fund
class Update(LoginRequiredMixin,FormView):
    template_name = "card/update.html"
    form_class = CardForm
    def form_valid(self, form):
        forms = form.save(commit=False)
        forms.owner = self.request.user
        User.objects.filter(username=self.request.user.username).update(fund=self.request.user.fund+forms.mount if forms.action=="+" else exec('try:self.request.user.fund-forms.mount\nexcept:messages.success(self.request,("you dont have enough money!"))'))
        forms.save()
        return  redirect("card:home")
    def form_invalid(self, form):
        print(form.errors)

class History(ListView):
    template_name = "card/history.html"
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)
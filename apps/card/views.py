from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, FormView, ListView, DetailView)
from django.contrib import messages

import uuid

from accounts.models import User
from card.models import Transaction
from .forms import CardForm

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
        forms.token =  uuid.uuid4().hex.upper()[0:15]
        user = User.objects.filter(username=self.request.user.username).first()
        
        if forms.action == "+":
            user.fund= user.fund + forms.mount
        else:
            try:
                user.fund= user.fund - forms.mount
                
            except:
                messages.error(self.request, "You don't have enough money in your accounts")
        user.save()
        forms.save()

        messages.error(self.request, "Information saved")
        return  redirect("card:home")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid information")
        return redirect("card:home")

class History(ListView):

    template_name = "card/history.html"
    paginate_by = 5
    
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)

class HistoryDetail(DetailView):

    template_name = "card/history_detail.html"
    
    def get_object(self):
        token = self.kwargs.get('token')
        object = get_object_or_404(Transaction, token= token)
        return object
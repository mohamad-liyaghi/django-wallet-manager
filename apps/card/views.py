from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, FormView, ListView, DetailView)
from django.contrib import messages

import random

from accounts.models import User
from card.models import Transaction
from .forms import CardForm


class Home(LoginRequiredMixin,ListView):
    '''Simply return users card balance'''
    template_name = "card/home.html"
    context_object_name = "balance"

    def get_queryset(self):
        return self.request.user.balance


class Update(LoginRequiredMixin, FormView):
    '''Update balance of a card'''
    template_name = "card/update.html"
    form_class = CardForm

    def form_valid(self, form):
        forms = form.save(commit=False)
        forms.owner = self.request.user
        forms.token =  random.randint(1, 99999999999999)
        user = self.request.user
        
        if forms.action == "+":
            user.balance = user.balance + forms.amount
        else:
            if user.balance > forms.amount:
                user.balance = user.balance - forms.mount
            else:
                messages.error(self.request, "Sth went wrong, you dont have enough money in your card!")
                return redirect("card:home")

        user.save()
        forms.save()

        messages.error(self.request, "Information saved")
        return  redirect("card:home")

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong with your information...")
        return redirect("card:home")


class History(ListView):
    '''Show latest Transactions'''
    template_name = "card/history.html"
    paginate_by = 5
    context_object_name = "transactions"
    
    def get_queryset(self):
        return self.request.user.transactions.all()

class HistoryDetail(DetailView):

    template_name = "card/history_detail.html"
    
    def get_object(self):
        token = self.kwargs.get('token')
        object = get_object_or_404(Transaction, token= token)
        return object
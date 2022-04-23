from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,FormView,ListView,DetailView
from django.contrib import messages
from account.models import User
from card.models import Transaction
from .forms import CardForm
from account.forms import RegisterForm
# Create your views here.
class Home(LoginRequiredMixin,ListView):
    template_name = "card/home.html"
    def get_queryset(self):
        if self.request.user.fund == None:
            User.objects.filter(username=self.request.user.username).update(fund=0)
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
    paginate_by = 5
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)
class HistoryDetail(DetailView):
    template_name = "card/history_detail.html"
    def get_object(self):
        pk = self.kwargs.get('pk')
        object = get_object_or_404(Transaction, pk=pk)
        return object
from django import forms
from card.models import Transaction
class CardForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
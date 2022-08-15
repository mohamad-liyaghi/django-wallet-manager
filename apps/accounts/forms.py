from django import  forms
from  django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    fund = forms.CharField()
    class Meta:
        model = User
        fields = ("username","first_name","last_name","password1","password2","fund")
        help_texts = {
            'username': None,
            'password1' : None,
            'password2': None,
        }
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = "Enter a valid password like: 4020TrKu (dont use this!)"
        self.fields['password2'].help_text = 'confirm your password'
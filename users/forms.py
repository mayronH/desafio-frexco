"""Forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser

class SignUpForm(UserCreationForm):
    """Signup Form with Birthdate and no password validation"""
    password1 = forms.CharField(label=("Senha"), widget=forms.PasswordInput, required=False)
    password2 = None
    birthdate = forms.DateField(label=("Data de Nascimento"), localize="pt-BR", widget=forms.DateTimeInput, 
                                input_formats=[ '%d/%m/%Y', 
                                                '%d/%m/%y',
                                                '%m/%d/%Y',      
                                                '%m/%d/%y' ])
    
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('birthdate',)
        labels = {
            'username': "Usuário",
        }
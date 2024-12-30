from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']  # Use email as username field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email']
        self.fields['password1']
        self.fields['password2']

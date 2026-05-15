from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "name")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "username", "name", "is_active", "is_staff")

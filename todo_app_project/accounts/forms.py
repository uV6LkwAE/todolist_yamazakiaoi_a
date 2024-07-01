

from django.contrib.auth.forms import UserCreationForm
# Userを新しく作成することに特化したForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


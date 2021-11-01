from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.forms import ModelForm
from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Reg_User
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Reg_User
        fields = ('email',)


# class UserLogForm(forms.ModelForm):
#     reg_user = forms.ModelChoiceField(
#         queryset = Reg_User.objects.all(),
#         widget = autocomplete.ModelSelect2(url = 'city-autocomp')
#         )

#     class Meta:
#         model = Reg_User

#         fields = ['__all__']

# class UserRegistrationForm()
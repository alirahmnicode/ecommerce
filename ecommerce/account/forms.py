from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from .models import CustomUser, Profile


class BaseCustomUserForm(ModelForm):
    """
    this class created for add form-control class to all
    fields.
    """

    def __init__(self, *args, **kwargs):
        super(BaseCustomUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class CustomUserCreationForm(BaseCustomUserForm, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone",)


class CustomUserChangeForm(BaseCustomUserForm, UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("phone",)


class ProfileUpdateForm(BaseCustomUserForm, ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)

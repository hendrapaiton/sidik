from django import forms

from apps.user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
        ]
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter Username'
                }
            )
        }

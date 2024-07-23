from django import forms
from .models import CostumeUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CostumeUserCreationForm(forms.ModelForm):
    password_1 = forms.CharField(widget=forms.PasswordInput, label='password_1')
    password_2 = forms.CharField(widget=forms.PasswordInput, label='password_2')

    class Meta:
        model = CostumeUser
        fields = ('email',)

    def clean(self):
        cd = super().clean()
        password_1,  password_2 = cd.get('password_1'), cd.get('password_2')
        if password_1 and password_2 and password_1 != password_2:
            raise ValidationError('!!! password are not the same !!!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_1'])
        if commit:
            user.save()
        return user


class CostumeUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='want to change password? <a href="../password/">click here</a>')

    class Meta:
        model = CostumeUser
        fields = ('email',)

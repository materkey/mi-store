# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'


class CreateUser(CreateView):
    model = get_user_model()
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = 'main:main'


def user_details(request, pk=None):
    user = get_object_or_404(User.objects.all(), pk=pk)

    return render(request, 'users/user_details.html', {'user': user})


def cabinet(request):
    user = request.user

    return render(request, 'users/cabinet.html', {'user': user})

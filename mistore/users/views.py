# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

User = get_user_model()


def user_details(request, pk=None):
    user = get_object_or_404(User.objects.all(), pk=pk)

    return render(request, 'users/user_details.html', {'user': user})


def cabinet(request):
    user = request.user

    return render(request, 'users/cabinet.html', {'user': user})

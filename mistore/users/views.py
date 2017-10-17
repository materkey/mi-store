# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from users.models import User


def user_detail(request, pk=None):
    
    user = get_object_or_404(User.objects.all(), pk=pk )

    return render(request, 'users/user_detail.html', {'user' : user})

def cabinet(request, pk=None):
    
    user = get_object_or_404(User.objects.all(), pk=pk )

    return render(request, 'users/cabinet.html', {'user' : user})

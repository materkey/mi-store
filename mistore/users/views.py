# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from users.models import User

def user_details(request, pk=None):
    
    user = get_object_or_404(User.objects.all(), pk=pk )

    return render(request, 'users/user_details.html', {'user' : user})

def cabinet(request):
    
    user = request.user

    return render(request, 'users/cabinet.html', {'user' : user})

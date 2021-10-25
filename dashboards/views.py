
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.views.decorators.csrf import csrf_exempt 
import uuid,json,ast
from root.models import * 

# Create your views here.

# @login_required(login_url='/account/login/')
# def user_profile(request): 
#     pass
    # profile = Profile.objects.filter(user=request.user).first() 
    # context = {"profile":profile}
    
    # return  render(request, 'dashboards/user_profile.html',context=context)



 
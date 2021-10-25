
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt

import uuid,sys,django
from root.models import *
from dateutil import  parser
from django.core.files import File
 
 
 
 
@csrf_exempt
def insert_new_chore(request): 
    response = None
    try:
        if request.method=='POST': 
            print(request)
            ch = Chore_Table(
                chore_name          = request.POST['chore_name']  , 
                chore_code          = request.POST['chore_code']  ,
                cre_on              = parser.parse(request.POST['cre_on']) ,
                last_updt_on        = parser.parse(request.POST['last_updt_on']) ,
                cre_by              = request.POST['cre_by']  , 
                last_updt_by        = request.POST['last_updt_by']  , 
                category            = request.POST['category']   ,
                rank                = request.POST['rank']  , 
                points              = request.POST['points']  ,  
                background_color    = request.POST['background_color']  ,   
                icon                = File(open(str(request.POST['icon'] ),'rb'))
            )
            ch.save()
            response = f'Chore record saved successfully - {ch.id}'

    except Exception as e:
        response = str(e)
        print(response)
    return JsonResponse({
        "response":response,
    })



@csrf_exempt
def insert_new_transaction(request): 
    print(1)
    response = None
    try:
        if request.method=='POST': 
            trans = Transaction_Table(
                chore          = Chore_Table.objects.get(id=int(request.POST['chore'])) , 
                user           = User.objects.get(id=int(request.POST['user']))  ,
                date           = parser.parse(request.POST['date']) ,
                duration       = request.POST['duration']  ,  
                cre_on         = parser.parse(request.POST['cre_on']) ,
                last_updt_on   = parser.parse(request.POST['last_updt_on']) ,
                cre_by         = request.POST['cre_by']  , 
                last_updt_by   = request.POST['last_updt_by']  ,  

            )
            trans.save()
            response = f'Transaction record saved successfully - {trans.id}'
            print(response)

    except Exception as e:
        response = e
        print(e)
    return JsonResponse({
        "response": str(response),
    })


@csrf_exempt
def test(request):
    print(request.POST)
    return JsonResponse({
        "data":request.POST['chore_name']
    })
   
    # date            = models.DateTimeField(blank=True,null=True,default=datetime.now())
    # duration        = models.IntegerField(blank=True,default=None,null=True)
    # chore           = models.ForeignKey(Chore_Table,on_delete=models.CASCADE,blank=True,null=True)
    # user            = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    # cre_on          = models.DateTimeField(blank=True,null=True,default=datetime.now())
    # last_updt_on    = models.DateTimeField(blank=True,null=True,default=datetime.now())
    # cre_by          = models.CharField(max_length=1000,blank=True,default='System')
    # last_updt_by    = models.CharField(max_length=1000,blank=True,default='System')
   
 
# @login_required(login_url="login")
# def profile(request): 
#     return render(request,'accounts/profile.html')

  
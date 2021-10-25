
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# return  render(request, 'dashboards/user_profile.html',context=context)


def index(request):
    if 'points_cart_session' not in request.session : request.session['points_cart_session'] = []
    chore_list = list(Chore_Table.objects.filter(category=1).order_by('rank'))[:12]
    points_cart = request.session['points_cart_session']
    cart_data = []
    for id in [list(x.values())[0] for x in points_cart] :
        cart_data.append( Chore_Table.objects.get(id=id))
    points_cart = [list(x.keys())[0] for x in points_cart] 
    cart_data = [[x,y] for x,y in zip(points_cart,cart_data)] 
    context = {
        "chore_list"  : chore_list,
        "cart_data"   : cart_data ,
        "total_cart_chores" : len(points_cart)
    }
    return render(request, 'root/index.html', context)


def all_chore_list(request):
    if 'points_cart_session' not in request.session : request.session['points_cart_session'] = []
    chore_list = list(Chore_Table.objects.all().order_by('rank'))[:]
    points_cart = request.session['points_cart_session']
    cart_data = []
    for id in [list(x.values())[0] for x in points_cart] :
        cart_data.append( Chore_Table.objects.get(id=id))
    points_cart = [list(x.keys())[0] for x in points_cart] 
    cart_data = [[x,y] for x,y in zip(points_cart,cart_data)]
    context = {
        "chore_list"        : chore_list,
        "cart_data"         : cart_data,
        "total_cart_chores" : len(points_cart),
        "page_title"        : 'All Chores'
    }
    return render(request, 'root/index.html', context)






def points_cart_add(request):
    points_cart = request.session['points_cart_session']
    chore_id = request.GET['chore_id']
    points_cart.append({str(uuid.uuid4()):chore_id})
    request.session['points_cart_session'] = points_cart
    
    points_cart = request.session['points_cart_session']

    cart_data = []
    for id in [list(x.values())[0] for x in points_cart] :
        cart_data.append( list(Chore_Table.objects.filter(id=int(id)).values())[0]   )
        


    points_cart = [list(x.keys())[0] for x in points_cart] 
    cart_data = [[x,y] for x,y in zip(points_cart,cart_data)][::-1]
    return JsonResponse({
        "cart_data": cart_data
    })




def points_cart_delete(request):
    points_cart = request.session['points_cart_session']
    chore_id = request.GET['chore_id']
    points_cart = [x for x in points_cart if list(x.keys())[0]!=chore_id]
    request.session['points_cart_session'] = points_cart
    
    points_cart = request.session['points_cart_session']

    cart_data = []
    for id in [list(x.values())[0] for x in points_cart] :
        cart_data.append( list(Chore_Table.objects.filter(id=int(id)).values())[0]   )

    points_cart = [list(x.keys())[0] for x in points_cart] 
    cart_data = [[x,y] for x,y in zip(points_cart,cart_data)][::-1]
    
    return JsonResponse({
        "cart_data": cart_data
    })


def submit_chores(request):
    points_cart = request.session['points_cart_session']
    ids = [list(x.values())[0] for x in points_cart] 
    records = []
    for id in ids:
      records.append( Chore_Table.objects.get(id=int(id)) )
    
    
    user = User.objects.get(username="admin")
    
    Transaction_Table.objects.bulk_create([
      Transaction_Table(
        chore = x,
        user= user,
        duration = 300,
      ) 
    for x in records
    ])
    
    request.session['points_cart_session'] = []
    
    
    return JsonResponse({ 
    })





























def handler404(request, *args, **argv):
    return render(request, 'root/404_page.html', {}, status=404)


def handler500(request, *args, **argv):
    return render(request, 'root/404_page.html', {}, status=404)

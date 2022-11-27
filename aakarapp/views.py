from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
import pandas as pd
import numpy as np
from ranklist import df


## import data tables from database
from .models import TaskZero

# print(f"df from views : {df} ")

# Create your views here.

def home(request):
    return render(request, "home.html")

def compi(request):
    return render(request,"compi_front_final.html")

def dashboard(request):
    user = request.user
    data = SocialAccount.objects.get(user=user).extra_data
    email = data.get('email')
    name = data.get('name')
    name = name.split(" ")
    picture = data.get('picture')
    current_user_id = 220000 + user.id

    rank_list = np.array(df['CRID']=="AK"+str(current_user_id))
    crid = "AK"+str(current_user_id)
    rank = -1
    # print(rank_list)
    for i in range(len(rank_list)):
        if rank_list[i]:
            rank = i+1
            break
    
    is_filled = False
    objects = TaskZero.objects.all()
    current_obj = ''
    for obj in objects:
        if obj.crid == crid:
            is_filled=True
            current_obj = obj
            break

 
    return render(request, "dashboard.html", 
    {'email': email,
     "name":name[0], 
     "picture": picture, 
     "CRID":"AK"+str(current_user_id),
     "rank":rank, 
     "objects":objects,
     "is_filled": is_filled,
     "current_obj": current_obj
    })

def redirect_view(request):
    response = redirect('/home')
    return response


def updateProfile(request):
    if request.method == "POST":
        user = request.user
        username = user.username
        current_user_id = 220000 + user.id
        crid = "AK"+str(current_user_id)
        colgName = request.POST.get('colName', '')
        state = request.POST.get('state', '')
        mobileNo = request.POST.get('phoneNo','')
        dept = request.POST.get('dept', '')
        whatsappNo = request.POST.get('whatsNo','')
        pincode = request.POST.get('pin', '')
        address = request.POST.get('address', '')
        print(crid, username, colgName, state, mobileNo, whatsappNo, dept, pincode, address)
        is_filled = False
        objects = TaskZero.objects.all()
        current_obj = ''
        for obj in objects:
            if obj.crid == crid:
                is_filled = True
                current_obj = obj
                break
        if not is_filled:
            response = TaskZero(crid=crid, username=username, colgName=colgName, state=state, mobileNo=mobileNo,
                                whatsappNo=whatsappNo, dept=dept, pincode=pincode, address=address)
            response.save()
        else:
            objects = TaskZero.objects.get(crid=crid)
            objects.delete()
            response = TaskZero(crid=crid, username=username, colgName=colgName, state=state, mobileNo=mobileNo,
                                whatsappNo=whatsappNo, dept=dept, pincode=pincode, address=address)
            response.save()

    return  redirect('dashboard')



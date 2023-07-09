from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
# Create your views here.

#For Registering New User into App
@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        password =data.get('password')
        email = data.get('email')
        
        existing_phone = app_database.objects.filter(phone=phone).first()
        if existing_phone:
            return JsonResponse("Already User registred with this Number",safe=False)
        else:
            user = app_database(name=name,phone=phone,password=password,email=email)    #Adding into app_database
            user_global = global_database(name=name,phone=phone)                       #Adding into gloabal_database
            user_global.save()
            user.save()
            return JsonResponse('Registration Sucessfully',safe=False)
    else:
        return redirect('Invalid Credentials')

#For Creating Contact in the Phone
@csrf_exempt  
def createcontact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        
        existing_phone = contact.objects.filter(phone=phone).first()
        if existing_phone:
            contact.objects.filter(phone=phone).update(name=name)
            return JsonResponse('contact Renamed',safe=False)
        else:
            cont = contact(name=name,phone=phone)
            glob = global_database(name=name, phone=phone)                  # Adding details into Global database
            glob.save()
            cont.save()
            return JsonResponse('Contact Saved Sucessfully',safe=False)
        
#User Logging into Application
@csrf_exempt  
def userlogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_ = data.get('phone')
        pass_word = data.get('password')

        try:
            get_obj = app_database.objects.get(phone=phone_)
            if get_obj.password == pass_word:
                # Password matches
                return JsonResponse("Login Successful", safe=False)
            else:
                return JsonResponse("Check Phone or Password", safe=False)
        except app_database.DoesNotExist:
            return JsonResponse("Check phone or Password", safe=False)
    else:
        return redirect("Error")

#User Performing spam Clicks
@csrf_exempt      
def spam(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_ = data.get('phone')
        print(phone_)
        
        try:
            spam_ob = global_database.objects.get(phone=phone_)
            spam_ob.spam += 1                   #Incrementing Spams in global databse by each click
            spam_ob.save()
            print(spam_ob.spam)
            if spam_ob.spam>10:                 # If spam value greater that 10 updating to is_spam = true in Appdatabse
                spam_obj2 = app_database.objects.filter(phone=phone_).update(is_spam=True)
                contact.objects.filter(phone=phone_).update(is_spam=True)
                
            if spam_ob or spam_obj2:
                return JsonResponse("Contact Marked as Spam ",safe=False)
            else:
                return JsonResponse("Contact Does Not Exit",safe=False)
        except global_database.DoesNotExist:
            return JsonResponse("Contact Does Not Exist",safe=False)

#Search users By their Names
@csrf_exempt 
def search_by_name(request):
    if request.method =='GET':
        name_= request.GET.get('name', None)
    
        try:
            list_a = global_database.objects.all().filter(name=name_)              #If name completely presents
            list_b = global_database.objects.all().filter(name__icontains=name_).exclude(name=name_) # Psrtial Name presents
            responses = []
            for cont in list_a:
                responses.append({
                    'name':cont.name,
                    'phone':cont.phone,
                    'spam':cont.spam
                })
            for cont in list_b:
                responses.append({
                    'name':cont.name,
                    'phone':cont.phone,
                    'spam':cont.spam
                    
                })
            return JsonResponse(responses,safe=False)
        except global_database.DoesNotExist:
            return JsonResponse("No Database Found", safe=False)
                

# Searching users by their Phone Numbers       
@csrf_exempt 
def search_by_phone(request):
    if request.method =='GET':
        phone_= request.GET.get('phone', None)
        try:
            list_ph = global_database.objects.all().filter(phone=phone_)
            responses = []
            for phn in list_ph:
                responses.append({
                    'name':phn.name,
                    'phone':phn.phone,
                    'is_spam':phn.spam
                })
            if len(responses) is None:
                return JsonResponse("No Phone Number Found",safe=False)
            else:
                return JsonResponse(responses,safe=False)
        except global_database.DoesNotExist:
            JsonResponse("No Database Found",safe=False)
        
    
                   
            
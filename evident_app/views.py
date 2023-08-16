import json
import statistics
from telnetlib import STATUS
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import *
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,response
from .forms import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
# Create your views here.

# home view
class BaseView(TemplateView):
    template_name='evident_app/base.html'

# user creation form and view
class UserCreating(APIView):
    def post(self,request):
        print(request.data)
        serializer=UserSerializer(data={
                "first_name": request.data['first_name'],
                 "last_name": request.data['last_name'],
                 "user_name":  request.data['user_name'],
                 "email":  request.data['email'],
                 "password": request.data['password'],
        })
        if serializer.is_valid():
            user=serializer.save()
            user=authenticate(user_name=serializer.validated_data.get('user_name'),password=serializer.validated_data.get('password'))
            if user.is_authenticated:
                login(self.request,user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({'message':'user created successfully','status':'200','token':token.key})
        return Response({"status":'400','message':'something went wrong','data':serializer.errors})



class SignupForm(TemplateView):
    template_name='evident_app/signup.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form']=UsercreateForm()
        return context

    # def post(self,request):
    #    return redirect('login')
              
    #         serializer=UserSerializer(data={
    #              "first_name": form.cleaned_data['first_name'],
    #              "last_name": form.cleaned_data['last_name'],
    #              "user_name": form.cleaned_data['user_name'],
    #              "email": form.cleaned_data['email'],
    #              "password": form.cleaned_data['password1'],
    #         })
            
    #         if serializer.is_valid():
    #             user=serializer.save()
    #             user=authenticate(
    #                       user_name=serializer.validated_data.get('user_name'),
    #                       password=serializer.validated_data.get('password')

    #                     )
    #             if user :
    #               login(request,user)
    #               token,created=Token.objects.get_or_create(user=user)
                  
    #               return redirect('base')
    #         else:
    #             print(serializer.errors)     
    #      return Response({'message':'something went wrong'},status=400)
        

#####  LOGIN FORM ######

class Loginview(TemplateView):
    template_name='evident_app/login.html'

##### LOGIN API #######

class LoginApi(APIView):
    def post(self,request):

        try:
            data=request.data
            print(data)
            serializer=LoginSerializer(data={
                'user_name':data['username'],
                'password':data['password']
            })
            if serializer.is_valid():
                user_name=serializer.data['user_name']
                password=serializer.data['password']

                user=authenticate(user_name=user_name,password=password)
                if user:
                    login(self.request,user)
                    token,created=Token.objects.get_or_create(user=user)
                    request.session['auth_token']=token.key
                    return Response({
                        'messege':'success',
                        'status':'200',
                        'data':{
                            'token':token.key,
                            'user_name':user.user_name,
                            'user_id':user.id
                        }
                    })    
        except:
            return Response({
                        'messege':'bad request',
                        'status':'400',
                        'data':serializer.errors
                    })    
        
        return Response({
                        'messege':'bad request',
                        'status':'400',
                        'data':serializer.errors
                    }) 
##### USER LOGOUT ######    
class LogoutView(View):
    def get(self,request):

        logout(request)
        return redirect('base')   
    



###############  Input value saving to the data base ###############
class ValueSavingView(View):
    def post(self,request):
        try:
            user=request.user
            data=json.loads(request.body)
            numbers_sort=[int(num.strip()) for num in data['input_value'].split(',')]
            sorted_value=sorted(numbers_sort,reverse=True)
            store_value=(',').join(str(num) for num in sorted_value)
            cust_user=CustomUser.objects.get(id=user.id)
            print(type(cust_user.id))
            input_inc=InputValue.objects.create(user_id=cust_user.id,values=store_value)
            input_inc.save()
            return JsonResponse(
                {
                    'status':'success',
                    'message':'input value saved to the database',
                    'user':user.id,
                    
                    }
                    )
        except:
            return JsonResponse(
                {
                    'status':'failed',
                    'message':'something went work',
                    'user':user.id
                    }
                )

###############  API VIEW ###############

class InputApiView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            user=request.user
            input_inc=InputValue.objects.filter(user_id=user.id).order_by("-create_at")
            payload=[]
            for input in input_inc:
                data={
                    "timestamp":input.timestamp,
                    "input_values":input.values
                    
                }
                payload.append(data)
            return Response({
                "status":"success",
                "user_id":user.id,
                "payload":payload
            }) 
        except:
            return Response({
                "ststus":"faild",
                "messege":"something went wrong"
            })
        
    def post(self,request):
        return  Response()    
class UserApiView(APIView):
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        token=request.session.get('auth_token')

        print(token)
        base_url='http://127.0.0.1:8000'
        api_url=base_url+'/user-api/'
        header={
            'Authorization':f'Token {token}'
        }
        response=requests.get(api_url,headers=header)
        
        user=request.user
       
        if user.is_authenticated:
            print('user is authenticated')
            print(user.user_name)
            return Response({'messege':'got user data','data':{
                "username":user.user_name
            }})
        else:
            return Response({'messege':'faild','data':{}})
        
    def post(self,request):
        return Response()

class TestView(View):
    def get(self,request):
        user=request.user
        print(user)

        return HttpResponse()     
    
       
   

    
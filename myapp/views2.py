from functools import partial
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer



# Create your views here.

def viewjson(request):
    return JsonResponse('RESP API end point...', safe=False)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        # test = request.data['username']
        username = request.data['username']
        password = request.data['password']
        # user = User.objects.get(username=username)
        result = authenticate(username=username, password=password) 
        if result is not None:
            login(request, result)
            return JsonResponse({'succes': 'succes'}, safe=False)
            

        # # 자격증명이 유효하면 User객체, 아니면 None 반환
        # # print(request.POST)

        # if user is not None:
        #     print('로그인 성공')
        #     login(request, user)
        #     return JsonResponse({'succes': 'succes'}, safe=False)

        else:
            # 오류 출력
            print('비번틀림')
            #DRF
            # return render(request, "login/login.html")
            return JsonResponse({'Hello':'Hello'}, safe=False)

def logout_view(request):
    logout(request)
    #DRF
    # return redirect('/auth/login')

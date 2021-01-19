from django.shortcuts import render
from .models import User
from django.http import JsonResponse
# Create your views here.


# 회원 가입
def register(request):
    pass


# 이메일 중복 체크
def emailCheck(request):
    try:
        user = User.objects.get(user_email=request.GET['user_email'])
    except Exception as e:
        user = None
    result = {
        'result': 'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data': "not exist" if user is None else "exist"
    }
    return JsonResponse(result)


# 닉네임 중복 체크
def nicknameCheck(request):
    try:
        nickname = User.objects.get(user_nickname=request.GET['user_nickname'])
    except Exception as e:
        nickname = None
    result = {
        'result': 'success',
        # 'data' : model_to_dict(nickname)  # console에서 확인
        'data': "not exist" if nickname is None else "exist"
    }
    return JsonResponse(result)


# 회원 정보 가져오기
def getUser(request):
    pass


# 회원 정보 수정 (Nicname만 )
def updateUser(request):
    pass


# 회원 탈퇴
def deleteUser(request):
    pass

from django.shortcuts import render
from . import services
# Create your views here.


# 메인 페이지
# top3 모임 불러오기
def index(request):

    return render(request, 'joinus_app/index.html')


# 로그인 페이지 이동
def signupPage(request):
    return render(request, 'joinus_app/signup.html')


# 회원 가입 페이지 이동
def signinPage(request):
    return render(request, 'joinus_app/signin.html')


# 각 카테고리별 모임페이지 이동
def noticeboard(request):
    pass


# 로그인 체크
def loginCheck(request):
    pass

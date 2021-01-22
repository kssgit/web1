from django.shortcuts import render, redirect
from . import services
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# 다른 형제엡의 Model 참조
from django.apps import apps


# 메인 페이지
# top3 모임 불러오기
def index(request):

    return render(request, 'joinus_app/index.html')


# 로그인 페이지 이동
def signupPage(request):
    if request.session.get('user'):
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'joinus_app/signup.html')


# 로그아웃
def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('index'))


# 로그인 체크
def loginCheck(request):
    res_data = {}
    user_email = request.POST['user_email']
    user_pw = request.POST['user_pw']
    user = apps.get_model(app_label='member_app', model_name='user')
    res_data['error'] = ''
    try:
        user_check = user.objects.get(user_email=user_email)
    except user.DoesNotExist:
        res_data['error'] = '일치하는 이메일이 없습니다.'
       # 보류
        return render(request, 'joinus_app/signup.html', res_data)

    if user_pw != user_check.user_pw:
        res_data['error'] = '비밀번호가 일치하지 않습니다.'
        return render(request, 'joinus_app/signup.html', res_data)

    request.session['user'] = user_check.user_nickname
    request.session['user_id'] = user_check.u_id
    return HttpResponseRedirect(reverse('index'))


# 각 카테고리별 모임페이지 이동
def noticeboard(request):
    category = request.GET['category']

    # 여기에는 joinus 모델과 noticeboard 모델 데이터 처리후 값 return

    return render(request, 'joinus_app/category.html')

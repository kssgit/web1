from django.shortcuts import render
from .models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.apps import apps  # 다른 어플 모델 참조
# Create your views here.


def signin(request):
    return render(request, 'member_app/signin.html')


# 회원 가입
def register(request):
    user_email = request.POST['user_email']
    user_nickname = request.POST['user_nickname']
    user_pw = request.POST['user_pw']
    new_user = User(user_email=user_email,
                    user_nickname=user_nickname, user_pw=user_pw)
    new_user.save()
    # 다른 view 메서드 바로 참조 가능(url아님)
    return HttpResponseRedirect(reverse("signupPage"))


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


# 회원 페이지 이동 및 회원정보 가져오기
def memberPage(request):
    # 로그인 했는지 확인
    if request.session.get('user_id'):
        res_data = {}
        # 유저 정보 담기
        user_id = request.session.get('user_id')
        user_data = User.objects.get(u_id=user_id)
        res_data['user_data'] = user_data
        # ---
        # 생성한 모임 가져오기
        meeting = apps.get_model(
            app_label='noticeboard_app', model_name='Meetings')
        createMeet = meeting.objects.filter(m_manager_id=user_id)
        res_data['createMeet'] = createMeet

        # 가입한 모임 가져오기
        joinus = apps.get_model(app_label='joinus_app', model_name='Joinus')
        userjoin = joinus.objects.filter(u_id=user_id)
        meetname = []
        for m in userjoin:
            name = meeting.objects.get(m_id=m.m_id)
            meetname.append(name)
        res_data['userjoin'] = meetname
        return render(request, 'member_app/memberPage.html', res_data)
    else:
        return HttpResponseRedirect(reverse('signupPage'))


# 회원 정보 수정 (Nicname만 )
def updateUser(request):
    pass


# 회원 탈퇴
def deleteUser(request):
    pass

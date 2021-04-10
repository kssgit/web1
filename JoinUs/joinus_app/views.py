from django.shortcuts import render, redirect

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, response
from .models import Joinus
# 다른 형제엡의 Model 참조
from django.apps import apps
from django.db.models import Count
# 장고 로그아웃 관리
from django.contrib import auth
# 장고 비번 암호화 라이브러리
import hashlib


# 메인 페이지
# top 모임 불러오기
def index(request):
    res_data = {}
    # 가입관리 모델에서 조건에 맞는 모델 데이타 가져오기
    meetsTop3 = Joinus.objects.values('m_id').annotate(
        Count('u_id')).order_by('-u_id__count')
    meetings = []  # top 모임을 담을 list
    # noticeboard_app 모델 가져오기

    print(meetsTop3)

    meeting = apps.get_model(
        app_label='noticeboard_app', model_name='meetings')
    if meetsTop3:
        for index, meet in enumerate(meetsTop3):
            if index < 3:  # 상위3개 모임만 가져오게

                m = meeting.objects.get(m_id=meet['m_id'])
                meetings.append(m)
         
        res_data['Top3Meeting'] = meetings
    else:
        # 모든 모임에 가입자가 없다면 빈 list 출력
        res_data['Top3Meeting'] = meetings
    return render(request, 'joinus_app/index.html', res_data)


# 로그인 페이지 이동
def signinPage(request):
    if request.session.get('user'):
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'joinus_app/signin.html')


# 로그아웃
def logout(request):

    if request.session.get('user'):
        request.session.clear()
        auth.logout(request)  # 장고 auth 기능 사용
    return redirect('/signin')


# 로그인 체크
def loginCheck(request):
    res_data = {}  # 결과 데이터 담을 딕셔너리
    if request.method == 'POST':
        user_email = request.POST['user_email']
        user_pw = request.POST['user_pw']
        user = apps.get_model(app_label='member_app', model_name='user')
        res_data['error'] = ''
        try:
            user_check = user.objects.get(user_email=user_email)
        except user.DoesNotExist:
            # 일치하는 이메일이 없을 경우
            res_data['error'] = '일치하는 이메일이 없습니다.'
            return render(request, 'joinus_app/signin.html', res_data)
        # 로그인 유저비번 암호화
        encoded_pw = user_pw.encode()
        encrypeted_pw = hashlib.sha256(encoded_pw).hexdigest()
        if encrypeted_pw != user_check.user_pw:  # 입력한 이메일의 비번이 다를 경우
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
            return render(request, 'joinus_app/signin.html', res_data)

        # 이메일과 비번이 일치할 경우 세션에 닉네임과 유저번호 저장
        request.session['user'] = user_check.user_nickname
        request.session['user_id'] = user_check.u_id

        return HttpResponseRedirect(reverse('index'))
    else:
        res_data['error'] = '잘못된 경로로 로그인을 시도하였습니다.'
        return render(request, 'joinus_app/signin.html', res_data)


# 각 카테고리별 모임페이지 이동
def noticeboard(request):
    category = request.GET['category']
    # 해당 카테고리 모임번호를 가입자 순위순으로 가져오기
    try:
        # 해당 카테고리 top 모임 id 가져오기
        meets = Joinus.objects.filter(category=category).values(
            'm_id').annotate(Count('u_id')).order_by('-u_id__count')

        meeting = apps.get_model(
            app_label='noticeboard_app', model_name='meetings')
        meetingTop3 = []  # top모임을 담을 list
        meetingOthers = []  # top모임을 제외한 다른 모임들을 생성 순으로 담을 list
        m_id = []  # top모임 번호를 기록할 list
        if meets:
            for index, meet in enumerate(meets):
                if index < 3:  # top3까지만
                    meeting_top = meeting.objects.get(m_id=meet['m_id'])

                    m_id.append(meet['m_id'])
                    meetingTop3.append(meeting_top)
        else:
            # 가입자수가 아예없는 카테고리는 모임 생성 순으로 다 표시
            meetingnojoin = meeting.objects.filter(m_category=category)
            for m in meetingnojoin:
                meetingOthers.append(m)
            res_data = {"meetingOthers": meetingOthers, "category": category}
            return render(request, 'joinus_app/category.html', res_data)
        # Top3 순으로 정렬후 아래에 모임 생성 순(top3모임 빼고)으로 표시
        meetingother = meeting.objects.filter(m_category=category)
        for m in meetingother:
            if len(m_id) == 3:  # top모임이 3개인경우 해당 모임 아이디를 제외한 모임만 담기
                if m.m_id != m_id[0] and m.m_id != m_id[1] and m.m_id != m_id[2]:
                    meetingOthers.append(m)
            elif len(m_id) == 2:  # top모임이 2개인경우 해당 모임 아이디를 제외한 모임만 담기
                if m.m_id != m_id[0] and m.m_id != m_id[1]:
                    meetingOthers.append(m)
            elif len(m_id) == 1:  # top모임이 1개인경우 해당 모임 아이디를 제외한 모임만 담기
                if m.m_id != m_id[0]:
                    meetingOthers.append(m)
            else:  # top모임이 없는 경우
                meetingOthers.append(m)

        res_data = {'meetingTop3': meetingTop3,
                    "meetingOthers": meetingOthers, "category": category}
    except Exception:
        # 해당 카테고리에 모임이 등록되지 않았을 경우
        res_data = {}
    return render(request, 'joinus_app/category.html', res_data)

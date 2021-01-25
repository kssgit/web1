from django.shortcuts import render, redirect
from . import services
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Joinus
# 다른 형제엡의 Model 참조
from django.apps import apps
from django.db.models import Count


# 메인 페이지
# top3 모임 불러오기
def index(request):
    res_data = {}
    meetsTop3 = Joinus.objects.values('m_id').annotate(
        Count('u_id')).order_by('-u_id__count')

    meetings = []

    meeting = apps.get_model(
        app_label='noticeboard_app', model_name='meetings')
    if meetsTop3:
        for index, meet in enumerate(meetsTop3):
            if index < 3:
                print(meet['m_id'])
                m = meeting.objects.get(m_id=meet['m_id'])
                meetings.append(m)
        res_data['Top3Meeting'] = meetings
    else:
        res_data['Top3Meeting'] = meetings
    return render(request, 'joinus_app/index.html', res_data)


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
    # 해당 카테고리 모임번호를 가입자 순위순으로 가져오기
    try:
        meets = Joinus.objects.filter(category=category).values(
            'm_id').annotate(Count('u_id')).order_by('-u_id__count')

        meeting = apps.get_model(
            app_label='noticeboard_app', model_name='meetings')
        meetingTop3 = []
        meetingOthers = []
        if meets:
            for index, meet in enumerate(meets):
                if index < 3:  # top3까지만
                    meeting_top = meeting.objects.get(m_id=meet['m_id'])
                    meetingTop3.append(meeting_top)
        else:
            # 가입자수가 아예없는 카테고리는 모임 생성 순으로 전체 다 표시하게끔
            print("요리")
            meetingnojoin = meeting.objects.filter(m_category=category)
            for m in meetingnojoin:
                meetingOthers.append(m)
            res_data = {"meetingOthers": meetingOthers, "category": category}
            return render(request, 'joinus_app/category.html', res_data)
        # Top3 순으로 정렬후 아래에 모임 생성 순으로 표시
        meetingother = meeting.objects.filter(m_category=category)
        for m in meetingother:
            meetingOthers.append(m)

        res_data = {'meetingTop3': meetingTop3,
                    "meetingOthers": meetingOthers, "category": category}
    except Exception:
        res_data = {}
    return render(request, 'joinus_app/category.html', res_data)

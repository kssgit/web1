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

    res_data = {}
    # select count(u_id) as count , m_id from joinus where category='공부'GROUP by m_id order by count(u_id) desc;
    if 1 == int(request.GET['category']):
        meets = Joinus.objects.filter(category="요리").values(
            'm_id').annotate(Count('u_id')).order_by('-u_id__count')

        meeting = apps.get_model(
            app_label='noticeboard_app', model_name='meetings')
        meetingorder = []

        if meets:
            for meet in meets:
                meeting_top = meeting.objects.get(m_id=meet['m_id'])
                meetingorder.append(meeting_top)

        else:
            meeting_top = meeting.objects.filter(m_category="요리")
            for m in meeting_top:
                meetingorder.append(m)

        res_data = {'meetingorder': meetingorder}

    elif 2 == int(request.GET['category']):
        meets = Joinus.objects.filter(category="공부").values(
            'm_id').annotate(Count('u_id')).order_by('-u_id__count')

        meeting = apps.get_model(
            app_label='noticeboard_app', model_name='meetings')
        meetingorder = []

        if meets:
            for meet in meets:
                meeting_top = meeting.objects.get(m_id=meet['m_id'])
                meetingorder.append(meeting_top)

        else:
            meeting_top = meeting.objects.filter(m_category="공부")
            for m in meeting_top:
                meetingorder.append(m)
        res_data = {'meetingorder': meetingorder}

    elif 3 == int(request.GET['category']):
        meets = Joinus.objects.filter(category="스포츠").values(
            'm_id').annotate(Count('u_id')).order_by('-u_id__count')

        meeting = apps.get_model(
            app_label='noticeboard_app', model_name='meetings')
        meetingorder = []

        if meets:
            for meet in meets:
                meeting_top = meeting.objects.get(m_id=meet['m_id'])
                meetingorder.append(meeting_top)
        else:
            meeting_top = meeting.objects.filter(m_category="스포츠")
            for m in meeting_top:
                meetingorder.append(m)
        res_data = {'meetingorder': meetingorder}
    return render(request, 'joinus_app/category.html', res_data)

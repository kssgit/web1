from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Meetings
from django.apps import apps


# 모임 생성 페이지 이동
def createPage(request):
    # 로그인 여부 확인
    if request.session.get('user'):
        return render(request, 'noticeboard_app/noticeboard.html')
    else:
        return HttpResponseRedirect(reverse('signupPage'))


# 새로운 모임 생성
def createMeet(request):
    m_category = request.POST['m_category']
    m_name = request.POST['m_name']
    m_content = request.POST['m_content']
    m_body = request.POST['m_body']
    m_manager_id = request.session.get('user_id')
    m_url = request.POST['m_url']
    m_image = request.FILES['m_image']
    new_meet = Meetings(m_category=m_category, m_name=m_name, m_content=m_content, m_url=m_url, m_manager_id=m_manager_id,
                        m_body=m_body,  m_image=m_image)

    new_meet.save()
    # 나중에 등록한 모임 자세히 보기 페이지로 전환할 예정
    return HttpResponseRedirect(reverse('index'))


# 모임 수정시 모임 이름 중복 체크 (수정시 같은 이름은 사용할 수 있는 이름으로 return)
def updatemeetnameCheck(request):
    m_id = request.session.get('update')
    same = Meetings.objects.get(m_id=m_id)
    if request.GET['m_name'] != same.m_name:
        try:
            name = Meetings.objects.get(m_name=request.GET['m_name'])
        except Exception as e:
            name = None
        result = {
            'result': 'success',
            # 'data' : model_to_dict(name)  # console에서 확인
            'data': "not exist" if name is None else "exist"
        }
    else:
        result = {
            'result': 'success',
            # 'data' : model_to_dict(name)  # console에서 확인
            'data': "not exist"
        }
    return JsonResponse(result)


# 모임 생성시 이름 중복 체크
def meetnameCheck(request):

    try:
        name = Meetings.objects.get(m_name=request.GET['m_name'])
    except Exception as e:
        name = None
    result = {
        'result': 'success',
        # 'data' : model_to_dict(name)  # console에서 확인
        'data': "not exist" if name is None else "exist"
    }

    return JsonResponse(result)


# 모임 정보 수정 페이지 전환
def updateMeetCheck(request):
    if request.session.get('user'):
        res_data = {}
        id = request.GET['id']
        print(id)
        meeting = Meetings.objects.get(m_id=id)
        res_data['meeting'] = meeting
        # 세션에 수정할 게시판 번호 등록
        request.session['update'] = id
        return render(request, 'noticeboard_app/updatenotice.html', res_data)
    else:
        return HttpResponseRedirect(reverse('signupPage'))


# 모임 상세 정보 불러오기
# 없는 게시판 요청할 경우 없는 게시판 입니다 요청 띄우고
# 해당 카테고리로 가든 아님 요청 들어온 전 페이지로 가든
def getMeet(request):
    id = request.GET['id']
    # db에서 정보 불러오기
    res_data = {}
    meeting = Meetings.objects.get(m_id=id)
    # 유저정보에서 해당 개시글 작성자의 닉네임 가져오기
    member = apps.get_model(app_label='member_app', model_name='user')
    member_name = member.objects.get(u_id=meeting.m_manager_id)
    res_data['nickname'] = member_name.user_nickname
    res_data['meeting'] = meeting
    # 가입자수 가져오기
    # select count(u_id) from joinus where m_id=id;
    joinus = apps.get_model(
        app_label='joinus_app', model_name='joinus')
    join = joinus.objects.filter(m_id=id).count()
    res_data['count'] = join

    # 세션에 가입할 게시판 번호 등록
    request.session['join'] = id
    return render(request, 'noticeboard_app/getnoticeboard.html', res_data)


# 수정한 모임 정보 등록
def updateMeet(request):
    if request.session.get('user'):
        m_id = request.session.get('update')
        update_meet = Meetings.objects.get(m_id=m_id)
        if request.session.get('user_id') == update_meet.m_manager_id:
            m_name = request.POST['m_name']
            m_content = request.POST['m_content']
            m_body = request.POST['m_body']
            m_url = request.POST['m_url']
            try:
                m_image = request.FILES['m_image']
                update_meet.m_image = m_image
            except Exception:
                print("이미지 없음")
            finally:
                update_meet.m_name = m_name
                update_meet.m_content = m_content
                update_meet.m_body = m_body
                update_meet.m_url = m_url
                update_meet.save()
                # 수정이 완료되면 세션에 등록된 게시판 번호 삭제
                request.session.delete('update')
            return redirect('/notice/getMeet?id='+m_id)
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('signupPage'))


# 모임 가입
def joinMeet(request):
    # 가입된 유저인지 확인
    if request.session.get('user'):
        id = request.session.get('join')
        # 잘못된 경로로 게시판 작성자가 가입 못하게 하기 위한 방법
        check_join = Meetings.objects.get(m_id=id)
        if request.session.get('user_id') != check_join.m_manager_id:
            # 이미 가입된 유저가 다시 가입하는것을 방지 하기 위한 방법
            # joinus 모델 가져오기
            joinus = apps.get_model(
                app_label='joinus_app', model_name='joinus')
            try:
                # 해당 유저가 가입한 모임 id 들 가져오기
                joincheck = joinus.objects.filter(
                    u_id=request.session.get('user_id'))
                print("에러 안남")
                # 해당 유저가 가입한 모임들하고 비교후 있으면 해당 페이지로 리턴
                for join in joincheck:
                    # 알아두자 requset에서 들어오는 파라미터는 str 로 들어온다는 것을 ....
                    if join.m_id == int(id):
                        return redirect('/notice/getMeet?id='+id)
                raise Exception

            except Exception:
                # 가입한 모임이 없으면
                user_id = request.session.get('user_id')
                category = check_join.m_category
                new_joinus = joinus(
                    u_id=user_id, m_id=id, category=category)
                new_joinus.save()
                return redirect('/notice/getMeet?id='+id)
        else:
            return redirect('/notice/getMeet?id='+id)

    else:
        # 로그인 하지 않고 가입하면 로그인 페이지로 이동
        return HttpResponseRedirect(reverse('signupPage'))


# 모임 삭제
def deleteMeet(request):
    if request.session.get('user'):
        check_meet = Meetings.objects.get(m_id=request.GET['id'])
        if request.session.get('user_id') == check_meet.m_manager_id:
            check_meet.delete()
            # joinus 테이블의 해당 모임 id도 삭제
            joinus = apps.get_model(
                app_label='joinus_app', model_name='joinus')
            select_join = joinus.objects.get(m_id=request.GET['id'])
            select_join.delete()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('signupPage'))

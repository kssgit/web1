from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Meetings
from django.apps import apps


# 모임 생성 페이지 이동
def createPage(request):
    # 로그인 여부 확인
    if request.session.get('user'):
        return render(request, 'noticeboard_app/createnoticeboard.html')
    else:
        return HttpResponseRedirect(reverse('signinPage'))


# 새로운 모임 생성
def createMeet(request):
    if request.session.get('user'):
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
        # 등록한 모임페이지로 이동
        move_notice = Meetings.objects.get(
            m_category=m_category, m_manager_id=m_manager_id, m_name=m_name)
        m_id = move_notice.m_id
        return redirect('/notice/getMeet?category='+m_category+"&id="+str(m_id))
    else:
        return HttpResponseRedirect(reverse('signin'))


# 모임 수정시 모임 이름 중복 체크 (수정시 같은 이름은 사용할 수 있는 이름으로 return)-Ajax
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


# 모임 생성시 이름 중복 체크(Ajax)
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
        # 만약에 없는 모임 을 요청할 경우
        try:
            meeting = Meetings.objects.get(m_id=id)
            res_data['meeting'] = meeting
            # 세션에 수정할 게시판 번호 등록
            request.session['update'] = id
            return render(request, 'noticeboard_app/updatenotice.html', res_data)
        except Exception:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('signinPage'))


# 모임 상세 정보 불러오기
# 없는 게시판 요청할 경우 없는 게시판 입니다 요청 띄우고
# 해당 카테고리로 가든 아님 요청 들어온 전 페이지로 가든
def getMeet(request):
    id = request.GET['id']
    category = request.GET['category']
    # db에서 정보 불러오기
    res_data = {}
    try:
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
        res_data['category'] = category
        # 세션에 가입할 게시판 번호 등록
        res_data['m_id'] = id
        # 이미 가입한 유저 정보 확인
        checkjoin = joinus.objects.filter(u_id=request.session.get('user_id'))
        result = 1
        for m in checkjoin:
            if int(id) == m.m_id:
                result = 0
                break

        res_data['checkjoin'] = result
        return render(request, 'noticeboard_app/getnoticeboard.html', res_data)
    except Exception:
        # 잘못된 경로로 없는 모임 페이지를 요청할 경우
        return redirect("/noticeboard?category="+category)


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
                # 기존 이미지 파일 삭제후
                update_meet.m_image.delete()
                update_meet.m_image = m_image
            except Exception:
                # 이미지 변경을 하지 않았을 경우
                pass
            finally:
                update_meet.m_name = m_name
                update_meet.m_content = m_content
                update_meet.m_body = m_body
                update_meet.m_url = m_url
                update_meet.save()
            # 업데이트한 모임페이지로 이동
            return redirect('/notice/getMeet?category='+update_meet.m_category+"&id="+m_id)
        else:
            # 등록 유저 아이디와 수정 요청 유저 아이디가 일치 하지 않는다면 메인 페이지로 전환
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('signinPage'))


# 모임 가입
def joinMeet(request):
    # 가입된 유저인지 확인
    if request.session.get('user'):
        id = request.GET['m_id']
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

                # 해당 유저가 가입한 모임들하고 비교후 있으면 해당 페이지로 리턴
                for join in joincheck:
                    # 알아두자 requset에서 들어오는 파라미터는 str 로 들어온다는 것을 ....
                    if join.m_id == int(id):
                        return redirect('/notice/getMeet?category='+check_join.m_category+"&id="+id)
                raise Exception

            except Exception:
                # 가입한 모임이 없으면
                user_id = request.session.get('user_id')
                category = check_join.m_category
                new_joinus = joinus(
                    u_id=user_id, m_id=id, category=category)
                new_joinus.save()
                return redirect('/notice/getMeet?category='+check_join.m_category+"&id="+id)
        else:
            return redirect('/notice/getMeet?category='+check_join.m_category+"&id="+id)

    else:
        # 로그인 하지 않고 가입하면 로그인 페이지로 이동
        return HttpResponseRedirect(reverse('signinPage'))


# 모임 탈퇴
def meetSecede(request):
    if request.session.get('user_id'):
        u_id = request.session.get('user_id')
        joinus = apps.get_model(app_label='joinus_app', model_name='Joinus')
        deljoin = joinus.objects.get(
            u_id=u_id, m_id=request.GET['m_id'])

        deljoin.delete()
        return redirect('/notice/getMeet?category='+deljoin.category+"&id="+request.GET['m_id'])
    else:
        return HttpResponseRedirect(reverse('signinPage'))
    pass


# 모임 삭제
def deleteMeet(request):
    if request.session.get('user'):
        try:
            check_meet = Meetings.objects.get(m_id=request.GET['id'])
            # 삭제 요청하는 유저 번호와 해당 모임을 등록한 유저 번호가 일치하는지 확인
            if request.session.get('user_id') == check_meet.m_manager_id:
                check_meet.delete()
                # joinus 테이블의 해당 모임 id도 삭제
                joinus = apps.get_model(
                    app_label='joinus_app', model_name='joinus')
                select_join = joinus.objects.filter(m_id=request.GET['id'])
                select_join.delete()
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))
        # 해당 모임이 없을 때 요청이 들어온 경우
        except Exception:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('signinPage'))

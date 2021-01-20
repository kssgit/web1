from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Meetings

# Create your views here.

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
    print(m_category)
    m_body = request.POST['m_body']
    m_manager_name = request.session.get('user')
    m_image = request.FILES['m_image']
    new_meet = Meetings(m_category=m_category, m_name=m_name, m_content=m_content,
                        m_body=m_body, m_manager_name=m_manager_name, m_image=m_image)

    new_meet.save()
    return HttpResponseRedirect(reverse('index'))


# 모임 이름 중복 체크
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


# 모임 정보 수정
def updateMeet(request):
    pass


# 모임 상세 정보 불러오기
def getMeet(request):
    pass


# 모임 가입
def joinMeet(request):
    pass


# 모임 삭제
def deleteMeet(request):
    pass

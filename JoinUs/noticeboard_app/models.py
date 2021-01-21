from django.db import models
# 미디어 파일 삭제를 위한 모듈
# 장고 스펙문서에서는 models.py에서 관리 하는것을 추천하지 않는 다고 한다
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Meetings(models.Model):
    m_category = models.CharField(max_length=225, verbose_name='카테고리')
    m_name = models.CharField(
        max_length=225, verbose_name='모임 이름', unique=True)
    m_content = models.CharField(max_length=225, verbose_name='소제목')
    m_body = models.TextField(verbose_name='상세내용')
    m_manager_nickname = models.CharField(
        max_length=64, verbose_name='등록 유저 닉네임')
    m_url = models.CharField(max_length=225, verbose_name='카카오 오픈 채팅 주소')
    m_create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')
    m_image = models.ImageField(
        upload_to='images/', blank=True, null=False, verbose_name='이미지파일')


# 업로드된 파일이 있는 게시글을 삭제하거나 수정할 시 FileField에는 파일의 path만 담고 있기 때문에 Django MEDIA_ROOT에 저장된 파일자체는 삭제되거나 수정되지 않는다
# 따라서 아래 매서드를 이용해 이미지도 함께 삭제해준다
# 모임 삭제시 등록된 이미지 파일도 같이 삭제해준다
@receiver(post_delete, sender=Meetings)
def file_delete_action(sender, instance, **kwargs):
    instance.m_image.delete(False)

from django.db import models
import os.path
from django.conf import settings

# Create your models here.


class Meeting(models.Model):
    category = models.CharField(max_length=225, verbose_name='카테고리')
    title = models.CharField(max_length=225, verbose_name='타이틀')
    body = models.TextField(verbose_name='상세내용')
    manager_id = models.IntegerField(verbose_name='등록 유저')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    image = models.ImageField(
        upload_to='images/', blank=True, null=False, verbose_name='이미지파일')


class Meetings(models.Model):
    m_category = models.CharField(max_length=225, verbose_name='카테고리')
    m_name = models.CharField(max_length=225, verbose_name='모임 이름')
    m_content = models.CharField(max_length=225, verbose_name='소제목')
    m_body = models.TextField(verbose_name='상세내용')
    m_manager_name = models.CharField(max_length=64, verbose_name='등록 유저 닉네임')
    m_create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')
    m_image = models.ImageField(
        upload_to='images/', blank=True, null=False, verbose_name='이미지파일')
    # 업로드된 파일이 있는 게시글을 삭제하거나 수정할 시 FileField에는 파일의 path만 담고 있기 때문에 Django MEDIA_ROOT에 저장된 파일자체는 삭제되거나 수정되지 않는다
    # 따라서 아래 매서드를 이용해 이미지도 함께 삭제해준다
    # 모임 삭제시 등록된 이미지 파일도 같이 삭제해준다

    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Meetings, self).delete(*args, **kargs)

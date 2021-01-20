from django.db import models

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

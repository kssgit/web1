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

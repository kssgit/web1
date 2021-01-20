from django.db import models

# Create your models here.


class Join(models.Model):
    u_id = models.IntegerField(verbose_name='가입자 id')
    m_id = models.IntegerField(verbose_name='모임 id')
    join_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='가입 시간')


class Joinus(models.Model):
    u_id = models.IntegerField(verbose_name='가입자 id')
    m_id = models.IntegerField(verbose_name='모임 id')
    m_category = models.CharField(max_length=225, verbose_name='카테고리')
    join_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='가입 시간')

from django.db import models

# Create your models here.


# foreign 키를 사용
# 다른 app의 model을 사용하려면 모델이름 앞에 productions(해당 app이름) 사용 related_name은 해당 모델 이름
# 장고 스펙문서 참조
# https://docs.djangoproject.com/ko/3.1/ref/models/fields/
class Joinus(models.Model):
    user_nickname = models.ForeignKey(
        'member_app.User', related_name='user', on_delete=models.CASCADE, db_column="user_nickname")
    m_name = models.ForeignKey(
        'noticeboard_app.Meetings', related_name='meetings', on_delete=models.CASCADE, db_column="m_name")
    category = models.CharField(max_length=225, verbose_name='카테고리')
    join_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='가입 시간')

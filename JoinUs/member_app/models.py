from django.db import models

# Create your models here.


class User(models.Model):
    user_email = models.CharField(max_length=64, verbose_name='사용자이메일')
    user_nickname = models.CharField(max_length=64, verbose_name='사용자 닉네임')
    user_pw = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

# id
# user_email
# user_nickname
# user_pw
# registered_dttm

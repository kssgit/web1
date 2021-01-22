# Generated by Django 3.1.5 on 2021-01-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noticeboard_app', '0010_delete_meetings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_category', models.CharField(max_length=225, verbose_name='카테고리')),
                ('m_name', models.CharField(max_length=225, unique=True, verbose_name='모임 이름')),
                ('m_content', models.CharField(max_length=225, verbose_name='소제목')),
                ('m_body', models.TextField(verbose_name='상세내용')),
                ('m_manager_id', models.IntegerField(verbose_name='모임 생성 자 id')),
                ('m_url', models.CharField(max_length=225, verbose_name='카카오 오픈 채팅 주소')),
                ('m_create_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('m_image', models.ImageField(blank=True, upload_to='images/', verbose_name='이미지파일')),
            ],
        ),
    ]

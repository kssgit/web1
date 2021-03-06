# Generated by Django 3.1.5 on 2021-01-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_category', models.CharField(max_length=225, verbose_name='카테고리')),
                ('m_name', models.CharField(max_length=225, verbose_name='모임 이름')),
                ('m_content', models.CharField(max_length=225, verbose_name='소제목')),
                ('m_body', models.TextField(verbose_name='상세내용')),
                ('m_manager_name', models.CharField(max_length=64, verbose_name='등록 유저 닉네임')),
                ('m_create_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('m_image', models.ImageField(blank=True, upload_to='images/', verbose_name='이미지파일')),
            ],
        ),
    ]

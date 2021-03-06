# Generated by Django 3.1.5 on 2021-01-21 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0002_auto_20210120_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(max_length=64, unique=True, verbose_name='사용자 이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(max_length=64, unique=True, verbose_name='사용자 닉네임'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('joinus_app', '0013_delete_joinus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joinus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.IntegerField()),
                ('m_id', models.IntegerField()),
                ('category', models.CharField(max_length=225, verbose_name='카테고리')),
                ('join_dttm', models.DateTimeField(auto_now_add=True, verbose_name='가입 시간')),
            ],
        ),
    ]
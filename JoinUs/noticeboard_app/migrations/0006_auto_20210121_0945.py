# Generated by Django 3.1.5 on 2021-01-21 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard_app', '0005_meetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='m_name',
            field=models.CharField(max_length=225, unique=True, verbose_name='모임 이름'),
        ),
    ]

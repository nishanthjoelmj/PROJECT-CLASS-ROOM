# Generated by Django 3.2.1 on 2021-05-27 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEACHER',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classRoomName', models.CharField(max_length=25)),
                ('class_url', models.CharField(blank=True, max_length=2000)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacher')),
            ],
            options={
                'unique_together': {('teacher', 'classRoomName')},
            },
        ),
        migrations.CreateModel(
            name='StudentInClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacherclassroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('classId', 'student')},
            },
        ),
    ]
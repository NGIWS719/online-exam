from django.db import models
from onlineExam.major import *


# Create your models here.


class Student(models.Model):
    id = models.CharField('学号', max_length=20, primary_key=True)
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', max_length=4, choices=SEX, default='男')
    dept = models.CharField('学院', max_length=20, choices=DEPT, default='计算机科学与工程学院')
    major = models.CharField('专业', max_length=20, default='软件工程')
    password = models.CharField('密码', max_length=20, default='111')
    email = models.EmailField('邮箱', default='gpu0@qq.com')
    birth = models.DateField('出生日期', default='2020-01-02')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class PaperOver(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField('科目', max_length=20, default='')
    data = models.TextField('考试内容', max_length=255, default='1')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, default='')  # 添加外键

    class Meta:
        db_table = 'paper_over'
        verbose_name = '完成试卷'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Log(models.Model):
    OPERATE = (
        ("login", "登录"),
        ("exit", "退出"),
        ("exam", "考试"),
        ("score", "查询成绩"),
    )

    ldate = models.CharField("时间", max_length=30)
    luser = models.CharField("姓名", max_length=20)
    operate = models.CharField("操作", max_length=20, choices=OPERATE)

    def __str__(self):
        return self.luser

    class Meta:
        db_table = "log"
        verbose_name = "日志"
        verbose_name_plural = verbose_name

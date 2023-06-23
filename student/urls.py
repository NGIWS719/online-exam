from django.conf.urls import url
from . import views

urlpatterns = [
    # 学生首页
    url(r'^index$', views.studentLogin),
    # # 开始考试
    url(r'^startExam', views.startExam),
    # # 查看试卷
    url(r'^lookPaper', views.lookPaper),
    # # 查看成绩
    url(r'^calGrade', views.calGrade),
    # # 用户注册
    url(r'^register', views.register),
    # # 个人信息修改
    url(r'^update_info', views.updateInfo),

]

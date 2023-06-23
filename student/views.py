from django.shortcuts import render, redirect
from student import models
import teacher
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
# def index(request):
#     return render(request, 'index.html')
#
#
# def toIndex(request):
#     return render(request, 'index.html')
#

# 学生登陆 视图函数
# def studentLogin(username, password):
#     # 获取表单信息
#     stuId = username
#     # 通过学号获取该学生实体
#     try:
#         student = models.Student.objects.get(id=stuId)
#         if password == student.password:  # 登录成功
#             # 查询考试信息
#             pass
#             paper = teacher.models.Paper.objects.filter(major=student.major)
#             # 查询成绩信息
#             grade = teacher.models.Grade.objects.filter(sid=student.id)
#             # 渲染index模板
#             # return render(request, 'index.html', )
#             return ['studentLogin.html', {'student': student, 'paper': paper, 'grade': grade}]
#         else:
#             # return render(request, 'index.html', {'message': '密码不正确'})
#             return '学号或密码错误'
#     except:
#         return '学号不存在'


def studentLogin(request):
    if request.method == 'POST':
        info_dict = request.POST
        username = info_dict['username']
        password = info_dict['password']
        code = info_dict['code']
        if code.upper() == request.session['code'].upper():
            # if code.upper() != request.session['code'].upper():
            try:
                student = models.Student.objects.get(id=username)
                if password == student.password:  # 登录成功
                    paper = teacher.models.Paper.objects.filter(major=student.major)
                    grade = teacher.models.Grade.objects.filter(sid=student.id)
                    insert_log(student.name, '登录')
                    return render(request, 'studentLogin.html', {'student': student, 'paper': paper, 'grade': grade})
                    # return render(request, 'index.html', {'message': '密码错误'})
                return HttpResponse('密码错误')
            except:
                # return render(request, 'index.html', {'message': '用户名不存在'})
                return HttpResponse('用户名不存在')
            # return render(request, 'index.html', {'message': '验证码错误'})
        return HttpResponse('验证码错误')
    return HttpResponse('404 error')


def register(request):
    if request.method == "POST":
        info_dict = request.POST
        i = info_dict['userid']
        u = info_dict['r_username']
        p = info_dict['r_password']
        # 或者
        # i = request.POST.get('userid')
        # u = request.POST.get('r_username')
        # p = request.POST.get('r_password')
        try:
            x = models.Student.objects.get(id=i)
            return HttpResponse("该用户已存在")
        except:
            user_type = request.POST['r_user_type']
            # 如果选择学生注册
            if user_type == "1":
                if i != ' ':
                    # 暂时将一些字段在model中默认写死写死
                    models.Student.objects.create(id=i, name=u, password=p)  # 创建对象并保存到数据库中
            # 如果选择教师注册
            elif user_type == "2":
                if i != ' ':
                    # 暂时将一些字段在model中默认写死写死
                    teacher.models.Teacher.objects.create(id=i, name=u, password=p)  # 创建对象并保存到数据库中
            return HttpResponse("注册成功")
    return render(request, "register.html", {})


# 个人信息修改
def updateInfo(request):
    from django.db import connection
    if request.method == "POST":
        info_dict = request.POST
        # 获取请求到的数据
        i = info_dict['u_id']
        u = info_dict['u_username']
        s = info_dict['u_sex']
        e = info_dict['u_email']
        b = info_dict['u_birth']
        p = info_dict['u_password']
        # y, m, d = b.split('/')
        # import datetime
        # birth = datetime.date(int(y), int(m), int(d))

        # 判断输入值中是否包含空格
        if ' ' not in u and ' ' not in e and ' ' not in b and ' ' not in p:
            # cursor = connection.cursor()
            # sql = "update student set name = '%s', sex = '%s', password = '%s', email = '%s', birth = '%s' " \
            #       "where id = '%s'"
            # val = (u, s, p, e, b, i)
            # cursor.execute(sql, val)
            # try:
            #     connection.commit()
            # except Exception:
            #     connection.rollback()

            # 查询指定的学生数据对象
            stu = models.Student.objects.get(id=i)

            # 更新数据字段
            stu.name = u
            stu.sex = s
            stu.password = p
            stu.email = e
            stu.brith = b

            # 保存更新
            stu.save()
        return HttpResponse("修改成功")
    return render(request, 'update_info.html')


# 学生考试 的视图函数
def startExam(request):
    sid = request.GET.get('sid')
    subject1 = request.GET.get('subject')

    student = models.Student.objects.get(id=sid)
    paper = teacher.models.Paper.objects.filter(subject=subject1)
    # print(type(paper[0].pid.through.Paper_pid))
    paper_len = len(paper[0].pid.all())
    return render(request, 'exam.html',
                  {'student': student, 'paper': paper, 'subject': subject1, 'paper_len': paper_len,
                   'paper_score': paper_len * 5})


# 学生查看已答试卷
def lookPaper(request):
    import json
    sid = request.GET.get('sid')
    subject1 = request.GET.get('subject')
    student = models.Student.objects.get(id=sid)
    paper = teacher.models.Paper.objects.filter(subject=subject1)
    paper_len = len(paper[0].pid.all())
    print(paper)

    paper_over = models.PaperOver.objects.filter(subject=subject1, sid_id=sid).values('data')

    data = paper_over[0]['data']  # 获取 QuerySet 中的 data 字段值
    data_dict = json.loads(data)  # 将 JSON 字符串转换为字典类型
    print(data_dict)
    # ans_l = []
    # for data_key in data_dict.keys():
    #     # 通过题号获取答案
    #     ans = data_dict[data_key]
    #     ans_l.append(ans)    # 答案存入列表
    # print(ans_l)
    return render(request, 'lookPaper.html',
                  {'student': student, 'paper': paper, 'subject': subject1, 'paper_len': paper_len, 'data_dict': data_dict, 'paper_score': paper_len * 5})


# 计算由exam.html模版传过来的数据计算成绩
def calGrade(request):
    import json
    if request.method == 'POST':
        # 得到字典的值
        sid = request.POST.get('sid')
        subject1 = request.POST.get('subject')
        # 将数据切片得到所有题号加答案
        keys = request.POST.keys()
        dict_slice = {}
        for k in list(keys)[2:]:
            dict_slice[k] = request.POST[k]
        data = json.dumps(dict_slice)
        # print(data)
        # 将科目，学号和试题遍号答案写入
        models.PaperOver.objects.create(subject=subject1, data=data, sid_id=sid)
        # 重新生成Student实例，Paper实例，Grade实例，名字和index中for的一致，可重复渲染
        student = models.Student.objects.get(id=sid)
        paper = teacher.models.Paper.objects.filter(major=student.major)
        grade = teacher.models.Grade.objects.filter(sid=student.id)

        # 计算该门考试的学生成绩
        question = teacher.models.Paper.objects.filter(subject=subject1).values("pid").values('pid__id', 'pid__answer',
                                                                                              'pid__score')

        mygrade = 0  # 初始化一个成绩为0
        for p in question:
            qId = str(p['pid__id'])  # int 转 string,通过pid找到题号
            myans = request.POST.get(qId)  # 通过 qid 得到学生关于该题的作答
            # print(myans)
            okans = p['pid__answer']  # 得到正确答案
            # print(okans)
            if myans == okans:  # 判断学生作答与正确答案是否一致
                mygrade += p['pid__score']  # 若一致,得到该题的分数,累加mygrade变量

        # 向Grade表中插入数据
        teacher.models.Grade.objects.create(sid_id=sid, subject=subject1, grade=mygrade)
        # print(mygrade)
        # 重新渲染index.html模板
        return render(request, 'studentLogin.html', {'student': student, 'paper': paper, 'grade': grade})


# 向数据库中插入日志记录
def insert_log(user, operate):
    from django.db import connection
    import time
    ldate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    cursor = connection.cursor()
    sql = "insert into log values(null,%s,%s,%s) "
    val = (ldate, user, operate)
    cursor.execute(sql, val)
    try:
        connection.commit()
    except Exception:
        connection.rollback()


def logOut(request):
    del request.session['username']
    return HttpResponse('index.html')

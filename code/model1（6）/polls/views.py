from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Users,T_Datas,H_Datas
from polls.algorithm import al
from django.urls import reverse

def index(request):
    contain="Hello, this is an data-centered app designed for your health!"
    return render(request, "polls/index.html", {'contain':contain})

def input(request,Users_id):
    contain = Users_id
    return render(request, "polls/input.html", {'contain':contain})

def suggestions(request,Users_id):
    m = Users.objects.get(pk=Users_id)
    systolic = m.t_datas_set.filter()[0].td
    diastolic = m.t_datas_set.filter()[1].td
    bmi = m.h_datas_set.filter()[2].hd / (m.h_datas_set.filter()[1].hd * m.h_datas_set.filter()[1].hd)
    bmi = int(100*bmi)/100
    gender = 0
    if m.Users_gender == "male":
        gender = 1
    tem=[systolic,diastolic,m.t_datas_set.filter()[2].td,(m.h_datas_set.filter()[0].hd) / 2, bmi,gender]
    return render(request, "polls/suggestions.html", {'users': tem})

def output(request,Users_id):
    m=Users.objects.get(pk=Users_id)
    systolic = m.t_datas_set.filter()[0].td
    diastolic = m.t_datas_set.filter()[1].td
    blood_pressure_index = (systolic - diastolic) / diastolic
    bmi = m.h_datas_set.filter()[2].hd / (m.h_datas_set.filter()[1].hd * m.h_datas_set.filter()[1].hd)
    response=get_radar_figure([{"收缩压":systolic,"舒张压":diastolic,"空腹血糖":m.t_datas_set.filter()[2].td,"运动强度":(m.h_datas_set.filter()[0].hd)/2,"BMI":bmi*4}])
    return response

def store(request,Users_id):
    if request.method == "POST":
        op_t_datas(request,Users_id)
        op_h_datas(request,Users_id)
        users=Users.objects.get(pk=Users_id)
        return render(request, "polls/store.html", {'users':users})
    else:
        users = Users.objects.get(pk=Users_id)
        return render(request, "polls/store.html", {'users': users})

def op_users(request):
    m=Users()
    m.Users_name=request.POST.get("user","")
    m.Users_id=request.POST.get("ID","")
    m.Users_gender=request.POST.get("sex","")
    m.Password=request.POST.get("password","")
    m.save()

def op_t_datas(request,Users_id):
    m=Users.objects.get(pk=Users_id)
    m.t_datas_set.create(td=request.POST.get("td1",""))
    m.t_datas_set.create(td=request.POST.get("td2", ""))
    m.t_datas_set.create(td=request.POST.get("td3", ""))
    m.save()

def op_h_datas(request,Users_id):
    m=Users.objects.get(pk=Users_id)
    m.h_datas_set.create(hd=request.POST.get("hd1",""))
    m.h_datas_set.create(hd=request.POST.get("hd2", ""))
    m.h_datas_set.create(hd=request.POST.get("hd3", ""))
    m.save()

def login(request):
    if request.method == "GET":
        return render(request, 'polls/login.html')
    else:
        # 获取数据
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        #return HttpResponse('%s'%username)
        m = Users.objects.get(Users_name=username)
        # 校验
        try:
            # 如果成功，login
            if(m.Password==password):
                return HttpResponseRedirect(reverse("store", args=(m.Users_id,)))
            else:
                return render(request, 'polls/login.html', {"error": "用户名或密码输入错误,请重新尝试"})
        except:
            return render(request, 'polls/login.html', {"error": "用户名或密码输入错误,请重新尝试"})
        
def register(request):
    if request.method=='POST':
        m = Users()
        m.Users_name = request.POST.get("user", "")
        m.Users_id = request.POST.get("ID", "")
        m.Users_gender = request.POST.get("sex", "")
        m.Password = request.POST.get("password", "")
        m.save()
        return HttpResponseRedirect(reverse("input", args=(m.Users_id,)))
    else:
        return render(request, 'polls/register.html')

def get_radar_figure(results):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import io
    from django.http import HttpResponse

    results = [{"收缩压":90,"舒张压":60,"空腹血糖":70,"运动强度":37.5,"BMI":18.5*4},{"收缩压":130,"舒张压":90,"空腹血糖":100,"运动强度":200,"BMI":25*4}] + results
    plt.rcParams["font.sans-serif"]=["SimHei"]
    plt.rcParams["axes.unicode_minus"]=False
    data_length = len(results[0])

    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    result_data = [[v for v in result.values()] for result in results]
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(10, 6), dpi=100)
    ax = plt.subplot(111, polar=True)
    color_ = ['r','g','b']
    for i in range(len(results)):
        data_now = np.concatenate((result_data[i], [result_data[i][0]]))
        ax.plot(angles, data_now, color=color_[i])

    ax.set_thetagrids(angles*180/np.pi, labels)
    ax.set_theta_zero_location('N')
    ax.set_rlim(0, 200)
    ax.set_rlabel_position(270)
    ax.set_title("健康雷达图")
    plt.legend(["标准下限","标准上限","用户数据"], loc='best')
    plt.yticks(color='w')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    fig_data=buf.getvalue()
    response = HttpResponse(fig_data, content_type='image/png')
    return response

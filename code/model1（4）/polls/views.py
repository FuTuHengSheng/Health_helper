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

def output(request,Users_id):
    response=get_radar_figure([{"血压":111,"血糖":222,"avc":333,"dads":156,"HDAH":115,"JH":895}])
    return response
    '''name=al(Users_id)
    return render(request,"polls/output.html",{'name':name})'''

def store(request,Users_id):
    if request.method == "POST":
        op_t_datas(request,Users_id)
        op_h_datas(request,Users_id)
        users=Users.objects.get(pk=Users_id)
        return render(request, "polls/store.html", {'users':users})
    else:
        return HttpResponse("Wrong!")
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
    m.save()

def op_h_datas(request,Users_id):
    m=Users.objects.get(pk=Users_id)
    m.h_datas_set.create(hd=request.POST.get("hd1",""))
    m.h_datas_set.create(hd=request.POST.get("hd2", ""))
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
                return HttpResponseRedirect(reverse("input", args=(m.Users_id,)))
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
    import matplotlib.pyplot as plt
    import io
    from django.http import HttpResponse

    plt.rcParams["font.sans-serif"]=["SimHei"]
    plt.rcParams["axes.unicode_minus"]=False
    data_length = len(results[0])
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    result_data = [[v for v in result.values()] for result in results]
    data_now = np.concatenate((result_data[0], [result_data[0][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(10, 6), dpi=100)
    fig.suptitle("健康雷达图")
    ax1 = plt.subplot(121, polar=True)
    ax, data, name = [ax1], [data_now], ["Username"]
    for i in range(len(results)):
        for j in np.arange(0, 100+20, 20):
            ax[i].plot(angles, (data_length + 1)*[j], '-.', lw=0.5, color='black')
        for j in range(data_length):
            ax[i].plot([angles[j], angles[j]], [0, 1000], '-.', lw=0.5, color='black')
        ax[i].plot(angles, data[i], color='b')
        ax[i].spines['polar'].set_visible(False)
        ax[i].grid(False)
        for a, b in zip(angles, data[i]):
            ax[i].text(a, b+5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
        ax[i].set_thetagrids(angles*180/np.pi, labels)
        ax[i].set_theta_zero_location('N')
        ax[i].set_rlim(0, 1000)
        ax[i].set_rlabel_position(0)
        ax[i].set_title(name[i])

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    fig_data=buf.getvalue()
    response = HttpResponse(fig_data, content_type='image/png')
    return response
# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Users,T_Datas,H_Datas
from polls.algorithm import al

def index(request):
    contain="Hello, this is an data-centered app designed for your health!"
    return render(request, "polls/index.html", {'contain':contain})

def input(request,Users_id):
    return HttpResponse("I:This is %s."% Users_id)

def output(request,Users_id):
    name=al(Users_id)
    return render(request,"polls/output.html",{'name':name})

def store(request):
    if request.method == "POST":
        op_users(request)
        op_t_datas(request)
        op_h_datas(request)
        users=get_object_or_404(Users,pk=request.POST.get("ID",""))
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
def op_t_datas(request):
    m=Users.objects.get(pk=request.POST.get("ID",""))
    m.t_datas_set.create(td=request.POST.get("td1",""))
    m.t_datas_set.create(td=request.POST.get("td2", ""))
    m.save()

def op_h_datas(request):
    m=Users.objects.get(pk=request.POST.get("ID",""))
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
        op_users(request)
        return redirect("/polls/login/")
    else:
        return render(request, 'polls/register.html')
# Create your views here.

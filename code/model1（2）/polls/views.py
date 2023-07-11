from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
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
# Create your views here.

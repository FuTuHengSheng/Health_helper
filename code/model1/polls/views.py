from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Users,T_Datas,H_Datas

def index(request):
    contain="Hello, this is an data-centered app designed for your health!"
    return render(request, "polls/index.html", {'contain':contain})

def input(request,Users_id):
    return HttpResponse("I:This is %s."% Users_id)

def output(request,Users_id):
    return HttpResponse("O:This is %s."% Users_id)

def store(request):
    if request.method == "POST":
        op_users(request)
        op_t_datas(request)
        op_h_datas(request)
        ans='get it!'
        return render(request, "polls/store.html", {'ans':ans})
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

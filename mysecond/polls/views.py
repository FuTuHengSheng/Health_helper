from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        #获取数据
        username=request.POST.get("user")
        password=request.POST.get("pwd")
        #校验
        try:
            if username== 'admin' and password == "12345":
            #如果成功，login
                return  redirect("/index/")
            else:
                #否则，请求再次登录，加提示
                return  render(request,'login.html',{"error":"用户名或密码输入错误,请重新尝试"})
        except:
            return render(request,'login.html',{"error","用户名或密码输入错误,请重新尝试"})



    

def index(request):
    return render(request,'index.html')

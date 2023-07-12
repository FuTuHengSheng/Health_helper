from polls.models import Users,T_Datas,H_Datas
def al(n):
    q=Users.objects.get(pk=n)
    return q.Users_name
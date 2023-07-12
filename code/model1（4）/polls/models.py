from django.db import models

# Create your models here.
class Users(models.Model):
    Users_name = models.CharField(max_length=200)
    Users_id=models.CharField(max_length=5,primary_key=True)
    Users_gender=models.CharField(max_length=6,default="male")
    Password=models.CharField(max_length=200,default="12345")
    def __str__(self):
        return self.Users_name
class T_Datas(models.Model):
    users=models.ForeignKey(Users,on_delete=models.CASCADE)
    td=models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return str(self.td)
class H_Datas(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    hd = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return str(self.hd)
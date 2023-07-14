from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name='index'),
    path("<int:Users_id>/input",views.input,name='input'),
    path("<int:Users_id>/output",views.output,name='output'),
    path("<int:Users_id>/store",views.store,name='store'),
    path("store/",views.store,name='store'),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("shouye/",views.suggestions,name='suggestions')
]
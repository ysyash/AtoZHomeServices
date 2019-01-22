from django.urls import path
from AtoZdelivery.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(r'^home/$',home),
    url(r'^cust_login/$',cust_login),
    url(r'^task_login/$',task_login),
    url(r'^cust_auth/$',cust_auth_view),
    url(r'^task_auth/$',task_auth_view),
    url(r'^loggedin/$', loggedin),
    url(r'^invalidlogin/$',invalid),
    url(r'^signup_cust/$',signup_cust),
    url(r'^signup_cust_ht/$',signup_cust_ht),
    url(r'^signup_tasker/$',signup_tasker),
    url(r'^signup_tasker_ht/$',signup_tasker_ht)
]
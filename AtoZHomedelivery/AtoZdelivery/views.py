from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from AtoZdelivery.models import Customer,tasker


def home(request):
	return render(request,'home.html')

def cust_login(request):
	msg=''
	return render(request,'cust_login.html',{"msg":msg})

def task_login(request):
	return render(request,'task_login.html')

def cust_auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	#user =Customer.objects.filter(c_email_id=username,c_password=password)
	user = auth.authenticate(Customer.objects.filter(c_name=username,c_password=password))
	if not (Customer.objects.filter(c_name=username,c_password=password)).exists():
		return HttpResponseRedirect('/invalidlogin/')
	else:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin/')

def task_auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	print(password)
	temp=auth.authenticate(tasker.objects.filter(t_email=username,t_password=password))
	if not (tasker.objects.filter(t_email=username,t_password=password)).exists():
		return HttpResponseRedirect('/invalidlogin/')
	else:
		auth.login(request,temp)
		return HttpResponseRedirect('/loggedin/')


def loggedin(request):
	c={}
	c.update(csrf(request))
	return render_to_response('loggedin.html',c)

def invalid(request):
	return render_to_response('invalid.html')

def signup_cust(request):
	msg="successful signup..."
	h=Customer(c_name= request.POST.get('name'),c_password=request.POST.get('password'),c_email_id=request.POST.get('emailid'),c_phone_no=request.POST.get('phoneno'),c_address="hiii")
	h.save()
	return render(request,'signup_cust_ht.html',{"msg":msg})

def signup_cust_ht(request):
	return render(request, 'signup_cust_ht.html')

def signup_tasker(request):
	msg="successful signup..."
	h=tasker(t_name=request.POST.get('name'),t_password=request.POST.get('password'),t_phone_no=request.POST.get('phoneno'),t_email=request.POST.get('emailid'),t_rupee=request.POST.get('rupee'))	
	h.save()
	return render(request,'signup_tasker_ht.html',{"msg":msg})

def signup_tasker_ht(request):
	return render(request, 'signup_tasker_ht.html')
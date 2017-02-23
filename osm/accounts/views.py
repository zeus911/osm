
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from .models import User,UserGroup
from .decorators import login_required
import hashlib

# Create your views here.
class UserForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

def login(request):
	if request.method == 'POST':
		uspa = UserForm(request.POST)
		if uspa.is_valid():
			username = uspa.cleaned_data['username']
			password = uspa.cleaned_data['password']
			user = User.objects.filter(username__exact = username,password__exact = hashlib.sha1(password).hexdigest())
			if user:
				request.session['username'] = username
				return render(request,'base.html')
			else:
				return HttpResponseRedirect('/accounts/login/')
		else:
			return HttpResponseRedirect('/accounts/login/')
	else:
		uspa = UserForm()	
	return render(request,'accounts/login.html')	

def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return HttpResponseRedirect('/accounts/login')

@login_required
def groupmanage(request):
	a = []
	grouplist = UserGroup.objects.all()
	for group in grouplist:
		group_dict = {'groupid': '%d' % (group.id),'groupname': '%s' % (group.groupname)}
		a.append(group_dict)
	return render(request,'accounts/groupmanage.html',{'a':a})

@login_required
def groupadd(request):
	if request.method == "GET" and 'groupname' in request.GET:
		groupname = request.GET['groupname']
		try:
			UserGroup.objects.create(groupname="%s" % (groupname))
		except Exception, e:
			return HttpResponse("sss")
		else:
			return HttpResponseRedirect('/accounts/groupmanage')
	else:
		return render(request,'accounts/groupadd.html')


@login_required
def groupedit(request,groupid):
	if request.method == "GET" and 'groupname' in request.GET:
		update = UserGroup.objects.get(id=groupid)
		gname = request.GET['groupname']
		update.groupname ="%s" % (gname)
		update.save()
		return HttpResponseRedirect('/accounts/groupmanage')
	else:
		a = []	
		group_set = UserGroup.objects.get(id=groupid)
		group_dict = {"groupname": "%s" % (group_set.groupname),"id":groupid}
		a.append(group_dict)
		return	render(request,'accounts/groupedit.html',{'a':a})

@login_required
def groupdel(request,groupid):
	UserGroup.objects.get(id="%s" % (groupid)).delete()
	return HttpResponseRedirect('/accounts/groupmanage')


@login_required
def usermanage(request):
	a = []
	userlist = User.objects.all()
	for user in userlist:
		user_dict = {'userid': '%d' % (user.id),'groupname': '%s' % (user.groupname),'username': '%s' % (user.username)}
		a.append(user_dict)
	return render(request,'accounts/usermanage.html',{'a':a})


@login_required
def useredit(request,userid):
	if request.method == "POST":
		user_update = User.objects.get(id=userid)
		gname = request.POST['groupname']
		uname = request.POST['username']
		pword = request.POST['password']
		
		user_update.groupname = UserGroup.objects.get(groupname="%s" % (gname))	
		user_update.username = "%s" % (uname)
		user_update.password = "%s" % (hashlib.sha1(pword).hexdigest())
		user_update.save()

		return HttpResponseRedirect('/accounts/usermanage')
	else:
		a = []
		user_set = User.objects.get(id=userid)
		grouplist = UserGroup.objects.all()
		user_dict = {'groupname': '%s' %(user_set.groupname),'username': '%s' % (user_set.username),'password': '%s' % (user_set.password),'userid': '%d' %(user_set.id)}
		a.append(user_dict)
		return render(request,'accounts/useredit.html',{'a':a,'grouplist':grouplist})

@login_required
def useradd(request):
	if request.method == "GET" and 'username' in request.GET:
		uname = request.GET['username']
		gname = request.GET['groupname']
		pword = request.GET['password']

		User.objects.create(username=uname,groupname=UserGroup.objects.get(groupname="%s" % (gname)),password=hashlib.sha1(pword).hexdigest())
		return HttpResponseRedirect('/accounts/usermanage')
	else:
		grouplist = UserGroup.objects.all()
		return render(request,'accounts/useradd.html',{'grouplist':grouplist})

@login_required
def userdel(request,userid):
	User.objects.get(id=userid).delete()
	return HttpResponseRedirect('/accounts/usermanage')

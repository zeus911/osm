from django.conf.urls import include,url
from . import views

urlpatterns = [
	url(r'^$',views.login,name='init_login'),
	url(r'^login/',views.login,name='login'),
	url(r'^logout/',views.logout,name='logout'),
	url(r'^groupmanage/',views.groupmanage,name='groupmanage'),
	url(r'^groupadd/',views.groupadd,name='groupadd'),
	url(r'^groupdel/(?P<groupid>[^/]+)/$',views.groupdel,name='groupdel'),
	url(r'^groupedit/(?P<groupid>[^/]+)/$',views.groupedit,name='groupedit'),
	url(r'^usermanage/',views.usermanage,name='usermanage'),
	url(r'^useredit/(?P<userid>[^/]+)/$',views.useredit,name='useredit'),
	url(r'^useradd/$',views.useradd,name='useradd'),
	url(r'^userdel/(?P<userid>[^/]+)$',views.userdel,name='userdel'),

]

from django.shortcuts import render
from accounts.decorators import login_required
from .saltapi import *

# Create your views here.
@login_required
def key_list(request):
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})

@login_required
def key_accept_reject(request):
    action = request.GET['action'].encode('utf-8')
    match = request.GET['match'].encode('utf-8')
    if action == "accept":        
        api_key(fun='key.accept', match='%s' %(match), arg_num=1)        
    elif action == "reject":
        api_key(fun='key.reject', match='%s' %(match), arg_num=1)
    else:
        pass
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})


@login_required
def key_delete(request):
    match = request.GET['match'].encode('utf-8')
    api_key(fun='key.delete', match='%s' %(match), arg_num=1)
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})

# @login_required
# def key_reject(request):
#     match = request.GET['match']
#     api_key(fun='key.reject', match='%s' %(match), arg_num=1)
#     minions = api_key()['return'][0]['data']['return']
#     return render(request, 'saltstack/key_list.html', {'minions': minions})

@login_required
def match_arg(request):
    return render(request, 'saltstack/match_arg.html')

@login_required
def connect_test_exec(request):
    err_ip = {}
    minions = api_key()['return'][0]['data']['return']
    tgt = request.GET['tgt'].encode('utf-8')
    cmd = request.GET['cmd'].encode('utf-8')
    arg = request.GET['arg'].encode('utf-8')
    expr_form = request.GET['options'].encode('utf-8')
    #ip_list_real = connect_test_ip.split(',')
    connect_test_result = api_exec('%s' %(tgt),'%s' %(cmd),'%s' %(arg),'%s' %(expr_form))['return'][0]
    # for i in ip_list_real:
    #     if connect_test_result.has_key('%s' %(i)):
    #         pass
    #     elif str(i) == "":
    #         pass
    #     elif str(i) == "*":
    #         pass
    #     else:
    #         err_ip[i] = False
    return render(request, 'saltstack/key_list.html', {'connect_test_result': connect_test_result,'err_ip': err_ip,'minions': minions})


@login_required
def ip_list(request):
    ip_list_text = []
    ip_list = request.GET['ip_list']
    ip_list_get = ip_list.split('\r\n')
    for i in ip_list_get:
        i = i.strip()
        if i != '':
            ip_list_text.append(i)
        else:
            pass
    return render(request, 'saltstack/match_arg.html', {'ip_list_text': ip_list_text})

@login_required
def cmd_exec_html(request):
    return render(request, 'saltstack/cmd_exec.html')

@login_required
def cmd_exec(request):
    ip_list = request.GET['ip_list'].encode('utf-8')
    exec_module = "cmd.run"
    cmd_args = request.GET['cmd_args'].encode('utf-8')
    cmd_exec_result = api_exec('%s' %(ip_list), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)['return'][0]
    return render(request, 'saltstack/cmd_exec.html', {'cmd_exec_result': cmd_exec_result})

@login_required
def state_exec_html(request):
    return render(request, 'saltstack/state_exec.html')

@login_required
def state_exec(request):
    ip_list = request.GET['ip_list'].encode('utf-8')
    exec_module = "state.sls"
    state_args = request.GET['state_args'].encode('utf-8')
    state_exec_result = api_exec('%s' %(ip_list), '%s' %(exec_module) , arg='%s' %(state_args), arg_num=1)['return'][0]
    return render(request, 'saltstack/state_exec.html', {'state_exec_result': state_exec_result})

@login_required
def minion_service_start_html(request):
    return render(request, 'saltstack/minion_service_start.html')

@login_required
def minion_service_start(request):
    master_ip = settings.MASTER_IP
    exec_module = "cmd.run"
    cmd_args_null = ">/salt-ssh/gg"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args_null), arg_num=1)
    ip_list = request.GET['ip_list'].encode('utf-8')
    ip_list_real = ip_list.split(',')
    for i in ip_list_real:
        cmd_args = "echo '%s' >> /salt-ssh/gg" %(i)
        api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
    cmd_args = "sh /salt-ssh/ip.sh"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
    cmd_kill_args = "salt-ssh -ir '*' 'sudo killall salt-minion'"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_kill_args), arg_num=1)
    cmd_start_args = "salt-ssh -ir '*' 'sudo salt-minion -d'"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_start_args), arg_num=1)
    return render(request, 'saltstack/minion_service_start_ok.html')

@login_required
def minion_install_html(request):
    return render(request, 'saltstack/minion_install.html')

# @login_required
# def minion_install(request):
#     master_ip = settings.MASTER_IP
#     exec_module = "cmd.run"
#     cmd_args_null = ">/salt-ssh/gg"
#     api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args_null), arg_num=1)
#     ip_list = request.GET['ip_list']
#     ip_list_real = ip_list.split(',')
#     for i in ip_list_real:
#         cmd_args = "echo '%s' >> /salt-ssh/gg" %(i)
#         api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
#     cmd_args = "sh /salt-ssh/ip.sh"
#     api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
#     cmd_install_args = "salt-ssh -i '*' state.sls minions.install"
#     minion_install_result = api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_install_args), arg_num=1)['return'][0]['%s' %(settings.MASTER_IP)]
#     return render(request, 'saltstack/minion_install.html', {'minion_install_result': minion_install_result})


@login_required
def minion_install(request):
    install_type =  request.GET['install']
    master_ip = settings.MASTER_IP
    exec_module = "cmd.run"
    if install_type == "pre_install":
        cmd_install_args = "salt-ssh -i '*' state.sls minions.install test=True -v"
    else:
        cmd_install_args = "salt-ssh -i '*' state.sls minions.install"
    minion_install_result = api_exec('Server1', '%s' %(exec_module) ,'%s' %(cmd_install_args))['return'][0]['Server1']
    return render(request, 'saltstack/minion_install.html', {'minion_install_result': minion_install_result})
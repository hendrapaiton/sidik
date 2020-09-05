import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import register
from django.views.decorators.csrf import csrf_exempt

from apps.device.models import Device
from apps.user.forms import UserForm
from apps.user.models import User, Finger


def create(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/')
        else:
            return HttpResponse('Error in forms, click <a href="/user/">here</a> to go back')
    else:
        context = {
            'form': form,
            'menu': 'user',
        }
        return render(request, 'apps/user/form.html', context)


def read(request):
    users = User.objects.all()
    context = {
        'users': users,
        'menu': 'user',
    }
    return render(request, 'apps/user/index.html', context)


def update(request, id_user):
    user_id = int(id_user)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('/user/')
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('/user/')
    else:
        context = {
            'form': form,
            'menu': 'user',
        }
        return render(request, 'apps/user/form.html', context)


def delete(request, id_user):
    user_id = int(id_user)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('/user/')
    user.delete()
    return redirect('/user/')


def user_register(request):
    baseurl = 'http://localhost:8000'
    user_id = request.GET.get('user_id')
    sectkey = 'SecurityKey'
    limit = 15
    result = user_id + ';' + sectkey + ';' + str(limit) + ';' + baseurl + '/user/register/process;' + baseurl + '/device/getac'
    return HttpResponse(result)


@csrf_exempt
def process_register(request):
    reg = request.POST
    data = []
    for r in reg:
        data.append(r)
    data[0] = request.POST.get('RegTemp')
    if data[0] is not None:
        vstamp = data[0]
        sn = data[1]
        user_id = data[2]
        regtemp = data[3]
        try:
            device = Device.objects.get(sn=sn)
        except Device.DoesNotExist:
            device = None
        temp = device.ac + device.vkey + regtemp + sn + user_id
        salt = hashlib.md5(temp.encode('utf-8')).hexdigest()
        if str(vstamp).upper() == str(salt).upper():
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                user = None
            Finger(username=user, finger_data=regtemp).save()
        return HttpResponse('empty')
    else:
        HttpResponse('Parameter invalid..')


def user_verification(request):
    baseurl = 'http://localhost:8000'
    user_id = request.GET.get('user_id')
    try:
        finger = Finger.objects.get(username__id=user_id)
    except Finger.DoesNotExist:
        finger = ''
    sectkey = 'SecurityKey'
    limit = 10
    result = user_id + ';' + finger.finger_data + ';' + sectkey + ';' + str(limit) + ';' + baseurl + '/user/verification/process;' + baseurl + '/device/getac;extraParams'
    return HttpResponse(result)


@csrf_exempt
def process_verification(request):
    baseurl = 'http://localhost:8000'
    ver = request.POST
    data = []
    for v in ver:
        print(v)
        data.append(v)
    data[0] = request.POST.get('VerPas')
    if data[0] is not None:
        user_id = data[0]
        vstamp = data[1]
        time = data[2]
        sn = data[3]
        try:
            fingerdata = Finger.objects.get(username__id=user_id)
        except Finger.DoesNotExist:
            fingerdata = None
        try:
            device = Device.objects.get(sn=sn)
        except Device.DoesNotExist:
            device = None
        user_name = fingerdata.username.username
        temp = sn + fingerdata.finger_data + device.vc + time + user_id + device.vkey
        salt = hashlib.md5(temp.encode('utf-8')).hexdigest()
        if str(vstamp).upper() == str(salt).upper():
            return HttpResponse(baseurl + '/log/message?user_name=' + user_name + '&time=' + time)
        else:
            return HttpResponse(baseurl + '/log/message?msg=error')
    else:
        msg = 'Parameter invalid..'
        return HttpResponse(msg)


@register.filter(name='finger_template')
def finger_template(value):
    finger = Finger.objects.filter(username__id=value).exists()
    if finger:
        return 1
    else:
        return 0

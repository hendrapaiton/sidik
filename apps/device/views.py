from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.device.forms import DeviceForm
from apps.device.models import Device


def create(request):
    form = DeviceForm()
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/device/')
        else:
            return HttpResponse('Error in forms, click <a href="/device/">here</a> to go back')
    else:
        context = {
            'form': form,
            'menu': 'device'
        }
        return render(request, 'apps/device/form.html', context)


def read(request):
    devices = Device.objects.all()
    context = {
        'devices': devices,
        'menu': 'device'
    }
    return render(request, 'apps/device/index.html', context)


def update(request, id_device):
    device_id = int(id_device)
    try:
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        return redirect('/device/')
    form = DeviceForm(request.POST or None, instance=device)
    if form.is_valid():
        form.save()
        return redirect('/device/')
    else:
        context = {
            'form': form,
            'menu': 'device'
        }
        return render(request, 'apps/device/form.html', context)


def delete(request, id_device):
    device_id = int(id_device)
    try:
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        return redirect('/device/')
    device.delete()
    return redirect('/device/')


def getac(request):
    vc = request.GET.get('vc')
    try:
        device_acsn = Device.objects.get(vc=vc)
        return HttpResponse(device_acsn.ac + device_acsn.sn)
    except Device.DoesNotExist:
        return HttpResponse('empty')

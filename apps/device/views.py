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
            return HttpResponse('Kesalahan dalam formulir, tekan <a href="/device">disini</a> untuk kembali')
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

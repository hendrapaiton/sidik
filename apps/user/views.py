from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.user.forms import UserForm
from apps.user.models import User


def create(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/')
        else:
            return HttpResponse('Kesalahan dalam formulir, tekan <a href="/device">disini</a> untuk kembali')
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

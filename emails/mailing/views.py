from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import EmailPostForm


# Create your views here.


def index(request):
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['email'],
                             form.cleaned_data['comment'],
                             'test.test.test.django.test@yandex.ru',
                             ['soloviov.sergei2018@yandex.ru'],
                             )
            if mail:
                messages.success(request, 'Mailed')
                return redirect('/')
            else:
                messages.error(request, 'error')
    else:
        form = EmailPostForm()
    return render(request, 'mailing/index.html', {"form": form})

from django.contrib.auth import login, logout  # Kullanıcının giriş yapabilmesi için login fonksiyonu
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import TemplateDoesNotExist


def register(request):
    """Register a new user."""
    if request.method != 'POST':  # Boş form açılır
        form = UserCreationForm()
    else:  # Kullanıcı formu doldurup göndermiştir.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()  # Form geçerli ise, formdaki bilgilerle bir kullanıcı oluştur ve veritabanına kaydet
            login(request, new_user)  # Oturum açar.
            return redirect('PollApp:home')  # Kullanıcı ana sayfaya yönlendirilir.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_success(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def login(request):
    login(request)
    return render(request, 'registration/login.html')
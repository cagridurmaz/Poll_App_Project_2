from django.contrib.auth import login    # Kullanıcının giriş yapabilmesi için login fonksiyonu
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    """Register a new user."""
    if request.method != 'POST':    # Boş form açılır
        form = UserCreationForm()
    else:                           # Kullanıcı formu doldurup göndermiştir.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()    # Form geçerli ise, formdaki bilgilerle bir kullanıcı oluştur ve veritabanına kaydet
            login(request, new_user)  # Oturum açar.
            return redirect('PollApp:home')  # Kullanıcı ana sayfaya yönlendirilir.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

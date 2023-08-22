from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),   # Kullanıcı girişi, çıkışı ve şifre sıfırlama işlemleri
    path('register/', views.register, name='register')   # Registration page
]

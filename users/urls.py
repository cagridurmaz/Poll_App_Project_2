from django.urls import path, include
from users import views

from django.contrib.auth.views import LogoutView




app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),   # Kullanıcı girişi, çıkışı ve şifre sıfırlama işlemleri
    path('register/', views.register, name='register'),  # Registration page
    path('logged_out/', views.logout_success, name='logout'),
    path('login/', views.login, name='login'),

]

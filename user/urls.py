from django.urls import path

from user import views


urlpatterns = [
    path('singup/', views.SignUp.as_view(template_name='signup.html'), name='signup'),
    #path('uyeguncelle/', views.Uye.as_view(template_name='uyeguncelle.html'), name='user_edit'),
    path('', views.Home, name='home'),
]
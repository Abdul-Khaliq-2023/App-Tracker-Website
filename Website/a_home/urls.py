from django.urls import path
from . import views

urlpatterns = [
    path('a_home/', views.appPage, name='a_home'),
    path('login/', views.loginpage, name='a_home'),
    path('save-data/', views.save_data, name='save_data'),
]
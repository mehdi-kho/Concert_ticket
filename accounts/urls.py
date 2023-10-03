from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.loginView),  # اگر بعد login اسلش نگذاریم (ادامه در پایین)
    path('logout/', views.logoutView),
    path('profile/', views.profileView),
    # path('profileRegister/', views.profileRegisterView),
    path('profileRegister', views.profileRegisterView),
    path('profileEdit', views.profileEditView),
]

# اگر بعد login اسلش  نگذاریم اگر درخواست کاربر یا ما بعد login ادامه داشته باشد مثل مثال زیر ارور می دهد
# http://127.0.0.1:8000/accounts/login/?next=/ticketSales/time/list
# http://127.0.0.1:8000/accounts/login/?next=/ticketSales/time/list

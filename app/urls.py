from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('create-diet-chart/', views.create_diet_chart, name='create_diet_chart'),
    path('choose-trainer/', views.choose_trainer, name='choose_trainer'),
    path('make-payment/', views.make_payment, name='make_payment'),
]
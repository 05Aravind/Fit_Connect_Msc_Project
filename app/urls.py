from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    # Trainer URLs
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/<int:pk>/', views.trainer_detail, name='trainer_detail'),
    path('trainers/create/', views.trainer_create, name='trainer_create'),
    path('trainers/<int:pk>/update/', views.trainer_update, name='trainer_update'),
    path('trainers/<int:pk>/delete/', views.trainer_delete, name='trainer_delete'),

    # WorkoutPlan URLs
    path('workoutplans/', views.workoutplan_list, name='workoutplan_list'),
    path('workoutplans/<int:pk>/', views.workoutplan_detail, name='workoutplan_detail'),
    path('workoutplans/create/', views.workoutplan_create, name='workoutplan_create'),
    path('workoutplans/<int:pk>/update/', views.workoutplan_update, name='workoutplan_update'),
    path('workoutplans/<int:pk>/delete/', views.workoutplan_delete, name='workoutplan_delete'),

    # FitnessActivity URLs
    path('fitnessactivities/', views.fitnessactivity_list, name='fitnessactivity_list'),
    path('fitnessactivities/<int:pk>/', views.fitnessactivity_detail, name='fitnessactivity_detail'),
    path('fitnessactivities/create/', views.fitnessactivity_create, name='fitnessactivity_create'),
    path('fitnessactivities/<int:pk>/update/', views.fitnessactivity_update, name='fitnessactivity_update'),
    path('fitnessactivities/<int:pk>/delete/', views.fitnessactivity_delete, name='fitnessactivity_delete'),

    # DietChart URLs
    path('dietcharts/', views.dietchart_list, name='dietchart_list'),
    path('dietcharts/<int:pk>/', views.dietchart_detail, name='dietchart_detail'),
    path('dietcharts/create/', views.dietchart_create, name='dietchart_create'),
    path('dietcharts/<int:pk>/update/', views.dietchart_update, name='dietchart_update'),
    path('dietcharts/<int:pk>/delete/', views.dietchart_delete, name='dietchart_delete'),

    # Payment URLs
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('payments/create/', views.payment_create, name='payment_create'),
    path('payments/<int:pk>/update/', views.payment_update, name='payment_update'),
    path('payments/<int:pk>/delete/', views.payment_delete, name='payment_delete'),
]
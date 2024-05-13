# app/admin.py

from django.contrib import admin
from .models import CustomUser, Trainer, WorkoutPlan, FitnessActivity, DietChart, Payment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('age', 'gender', 'height', 'weight')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone', 'email', 'training_approach')

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'userid', 'duration', 'start_date', 'end_date')


@admin.register(FitnessActivity)
class FitnessActivityAdmin(admin.ModelAdmin):
    list_display = ('type', 'userid', 'duration', 'activity_date', 'calories_burned')

@admin.register(DietChart)
class DietChartAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'userid', 'quantity', 'timing', 'description')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('userid', 'amount', 'payment_date', 'payment_method')


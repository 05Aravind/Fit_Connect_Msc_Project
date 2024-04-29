# app/admin.py

from django.contrib import admin
from .models import CustomUser, Trainer, WorkoutPlan, FitnessActivity, DietChart, Payment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'gender', 'height', 'weight')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone', 'email', 'training_approach')

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'duration', 'start_date', 'end_date')

    def user(self, obj):
        return obj.userid.username

@admin.register(FitnessActivity)
class FitnessActivityAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'duration', 'activity_date', 'calories_burned')

    def user(self, obj):
        return obj.userid.username

@admin.register(DietChart)
class DietChartAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'user', 'quantity', 'timing', 'description')

    def user(self, obj):
        return obj.userid.username

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_date', 'payment_method')

    def user(self, obj):
        return obj.userid.username
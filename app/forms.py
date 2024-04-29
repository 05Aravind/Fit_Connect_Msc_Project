from django import forms
from .models import CustomUser, Trainer, WorkoutPlan, FitnessActivity, DietChart, Payment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'gender', 'height', 'weight']
        # Add any additional fields or customizations you need

    def save(self, commit=True):
        user = super().save(commit=False)
        # user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['activityid', 'name', 'specialty', 'phone', 'email', 'training_approach']

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['userid', 'title', 'description', 'duration', 'start_date', 'end_date']

class FitnessActivityForm(forms.ModelForm):
    class Meta:
        model = FitnessActivity
        fields = ['userid', 'type', 'duration', 'activity_date', 'calories_burned']

class DietChartForm(forms.ModelForm):
    class Meta:
        model = DietChart
        fields = ['userid', 'food_name', 'quantity', 'timing', 'description']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['userid', 'amount', 'payment_date', 'payment_method']
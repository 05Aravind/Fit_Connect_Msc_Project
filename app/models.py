from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CustomUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    REQUIRED_FIELDS = [ 'email', 'age', 'gender', 'height', 'weight']

class Trainer(models.Model):
    trainerid = models.IntegerField(primary_key=True)
    activityid = models.IntegerField()
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    training_approach = models.CharField(max_length=100)

class WorkoutPlan(models.Model):
    planid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

class FitnessActivity(models.Model):
    activityid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    activity_date = models.DateField()
    calories_burned = models.DecimalField(max_digits=7, decimal_places=2)

class DietChart(models.Model):
    dietid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    description = models.TextField()

class Payment(models.Model):
    paymentid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)
    payment_method = models.CharField(max_length=50)


from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser, Trainer, WorkoutPlan, FitnessActivity, DietChart, Payment
from .forms import UserForm, TrainerForm, WorkoutPlanForm, FitnessActivityForm, DietChartForm, PaymentForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import date

@login_required
def upload_meal(request):
    if request.method == 'POST':
        form = DietChartForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.userid = request.user
            meal.activity_date = date.today()
            meal.save()
            return redirect('home')  # You can redirect to any other page after meal upload
    else:
        form = DietChartForm()
    return render(request, 'upload_meal.html', {'form': form})


def home(request):
    return render(request, 'home.html')

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home.html')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


# User Views
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    user.delete()
    return redirect('user_list')

# Trainer Views
def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

def trainer_detail(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return render(request, 'trainer_detail.html', {'trainer': trainer})

def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

def trainer_update(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', pk=pk)
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

def trainer_delete(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    trainer.delete()
    return redirect('trainer_list')

# WorkoutPlan Views
def workoutplan_list(request):
    workoutplans = WorkoutPlan.objects.all()
    return render(request, 'workoutplan_list.html', {'workoutplans': workoutplans})

def workoutplan_detail(request, pk):
    workoutplan = get_object_or_404(WorkoutPlan, pk=pk)
    return render(request, 'workoutplan_detail.html', {'workoutplan': workoutplan})

def workoutplan_create(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workoutplan_list')
    else:
        form = WorkoutPlanForm()
    return render(request, 'workoutplan_form.html', {'form': form})

def workoutplan_update(request, pk):
    workoutplan = get_object_or_404(WorkoutPlan, pk=pk)
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST, instance=workoutplan)
        if form.is_valid():
            form.save()
            return redirect('workoutplan_detail', pk=pk)
    else:
        form = WorkoutPlanForm(instance=workoutplan)
    return render(request, 'workoutplan_form.html', {'form': form})

def workoutplan_delete(request, pk):
    workoutplan = get_object_or_404(WorkoutPlan, pk=pk)
    workoutplan.delete()
    return redirect('workoutplan_list')

# FitnessActivity Views
def fitnessactivity_list(request):
    fitnessactivities = FitnessActivity.objects.all()
    return render(request, 'fitnessactivity_list.html', {'fitnessactivities': fitnessactivities})

def fitnessactivity_detail(request, pk):
    fitnessactivity = get_object_or_404(FitnessActivity, pk=pk)
    return render(request, 'fitnessactivity_detail.html', {'fitnessactivity': fitnessactivity})

def fitnessactivity_create(request):
    if request.method == 'POST':
        form = FitnessActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fitnessactivity_list')
    else:
        form = FitnessActivityForm()
    return render(request, 'fitnessactivity_form.html', {'form': form})

def fitnessactivity_update(request, pk):
    fitnessactivity = get_object_or_404(FitnessActivity, pk=pk)
    if request.method == 'POST':
        form = FitnessActivityForm(request.POST, instance=fitnessactivity)
        if form.is_valid():
            form.save()
            return redirect('fitnessactivity_detail', pk=pk)
    else:
        form = FitnessActivityForm(instance=fitnessactivity)
    return render(request, 'fitnessactivity_form.html', {'form': form})

def fitnessactivity_delete(request, pk):
    fitnessactivity = get_object_or_404(FitnessActivity, pk=pk)
    fitnessactivity.delete()
    return redirect('fitnessactivity_list')

# DietChart Views
def dietchart_list(request):
    dietcharts = DietChart.objects.all()
    return render(request, 'dietchart_list.html', {'dietcharts': dietcharts})

def dietchart_detail(request, pk):
    dietchart = get_object_or_404(DietChart, pk=pk)
    return render(request, 'dietchart_detail.html', {'dietchart': dietchart})

def dietchart_create(request):
    if request.method == 'POST':
        form = DietChartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dietchart_list')
    else:
        form = DietChartForm()
    return render(request, 'dietchart_form.html', {'form': form})

def dietchart_update(request, pk):
    dietchart = get_object_or_404(DietChart, pk=pk)
    if request.method == 'POST':
        form = DietChartForm(request.POST, instance=dietchart)
        if form.is_valid():
            form.save()
            return redirect('dietchart_detail', pk=pk)
    else:
        form = DietChartForm(instance=dietchart)
    return render(request, 'dietchart_form.html', {'form': form})

def dietchart_delete(request, pk):
    dietchart = get_object_or_404(DietChart, pk=pk)
    dietchart.delete()
    return redirect('dietchart_list')

# Payment Views
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payment_detail.html', {'payment': payment})

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_detail', pk=pk)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment_form.html', {'form': form})

def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('payment_list')
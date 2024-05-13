from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            custom_user = get_object_or_404(CustomUser, user_id=user)
            fitness_activities = FitnessActivity.objects.filter(userid=user)
            workout_plans = WorkoutPlan.objects.filter(userid=user)
            context = {
                'custom_user': custom_user,
                'fitness_activities': fitness_activities,
                'workout_plans': workout_plans,
            }
            return render(request, 'home.html', context)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, DietChart, Trainer, Payment, FitnessActivity, WorkoutPlan
from .forms import UserProfileForm, DietChartForm

@login_required
def home(request):
    user = request.user
    custom_user = get_object_or_404(CustomUser, user_id=user)
    fitness_activities = FitnessActivity.objects.filter(userid=user)
    workout_plans = WorkoutPlan.objects.filter(userid=user)
    diet_charts = DietChart.objects.filter(userid=user)
    context = {
        'custom_user': custom_user,
        'fitness_activities': fitness_activities,
        'workout_plans': workout_plans,
        'diet_charts': diet_charts,
    }
    return render(request, 'home.html', context)

@login_required
def update_profile(request):
    user = request.user
    custom_user = get_object_or_404(CustomUser, user_id=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=custom_user)
        if form.is_valid():
            form.save()
            # Add success message
            return redirect('home')
    else:
        form = UserProfileForm(instance=custom_user)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def create_diet_chart(request):
    if request.method == 'POST':
        form = DietChartForm(request.POST)
        if form.is_valid():
            diet_chart = form.save(commit=False)
            diet_chart.userid = request.user
            diet_chart.save()
            # Add success message
            return redirect('home')
    else:
        form = DietChartForm()
    return render(request, 'create_diet_chart.html', {'form': form})

@login_required
def choose_trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'choose_trainer.html', {'trainers': trainers})

@login_required
def make_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        # Process payment and create Payment object
        payment = Payment(userid=request.user, amount=amount, payment_method=payment_method)
        payment.save()
        # Add success message
        return redirect('home')
    return render(request, 'make_payment.html')
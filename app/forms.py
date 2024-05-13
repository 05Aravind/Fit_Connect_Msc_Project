from django import forms
from .models import CustomUser, Trainer, WorkoutPlan, FitnessActivity, DietChart, Payment

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, DietChart
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    height = forms.DecimalField(max_digits=5, decimal_places=2)
    weight = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'age', 'gender', 'height', 'weight')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            custom_user = CustomUser.objects.create(
                user_id=user,
                age=self.cleaned_data['age'],
                gender=self.cleaned_data['gender'],
                height=self.cleaned_data['height'],
                weight=self.cleaned_data['weight']
            )
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['age', 'gender', 'height', 'weight']

class DietChartForm(forms.ModelForm):
    class Meta:
        model = DietChart
        fields = ['food_name', 'quantity', 'timing', 'description']
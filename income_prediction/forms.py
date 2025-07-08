import datetime
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ModelForm
from django import forms
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class AccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'computations_count']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'computations_count': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }



class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'new-password'
            })


class PredictionInputForm(forms.Form):
    """
    Form for collecting prediction input parameters.

    Attributes:
        p1,p2,p12,p27,p28: Float fields for numerical parameters
        city_group: Choice field for city classification
        restaurant_type: Choice field for restaurant type
        days_open: Date field for opening date
    """

    P1 = forms.FloatField(label='m2 of the location', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P2 = forms.FloatField(label='Rating average cost of food', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P12 = forms.FloatField(label='Rating monthly marketing budget', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P27 = forms.FloatField(label='Number of school in the street', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P28 = forms.FloatField(label='Rating average table occupancy', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))


    CITY_GROUP_CHOICES = [
        ('Big Cities', 'Big Cities'),
        ('Other', 'Other'),
    ]

    RESTAURANT_TYPE_CHOICES = [
        ('FC', 'FC (Food Court)'),
        ('IL', 'IL (Inline)'),
        ('Other', 'Other'),
    ]

    city_group = forms.ChoiceField(
        label='City Group',
        choices=CITY_GROUP_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input'
        }),
        initial='Big Cities'
    )

    restaurant_type = forms.ChoiceField(
        label='Restaurant Type',
        choices=RESTAURANT_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        initial='FC'
    )

    days_open = forms.DateField(
        label='Open Date',
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'Select date',
            'autocomplete': 'off'
        }),
        input_formats=['%Y-%m-%d'],
        initial=datetime.date.today()
    )
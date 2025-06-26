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


# Дополнительно можно кастомизировать форму
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'new-password'
            })


class PredictionInputForm(forms.Form):
    # Числовые параметры
    P1 = forms.FloatField(label='P1', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P2 = forms.FloatField(label='P2', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P3 = forms.FloatField(label='P3', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P4 = forms.FloatField(label='P4', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P5 = forms.FloatField(label='P5', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P6 = forms.FloatField(label='P6', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P7 = forms.FloatField(label='P7', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P11 = forms.FloatField(label='P11', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P12 = forms.FloatField(label='P12', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P14 = forms.FloatField(label='P14', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P15 = forms.FloatField(label='P15', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P17 = forms.FloatField(label='P17', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P18 = forms.FloatField(label='P18', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P19 = forms.FloatField(label='P19', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P20 = forms.FloatField(label='P20', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P21 = forms.FloatField(label='P21', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P22 = forms.FloatField(label='P22', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P23 = forms.FloatField(label='P23', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P25 = forms.FloatField(label='P25', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P27 = forms.FloatField(label='P27', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P28 = forms.FloatField(label='P28', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P29 = forms.FloatField(label='P29', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P33 = forms.FloatField(label='P33', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))
    P37 = forms.FloatField(label='P37', min_value=0, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'step': '0.5'
    }))

    # Категориальные параметры
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
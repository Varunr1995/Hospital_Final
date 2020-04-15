from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# ----------- APPOINTMENT REQUEST FORM -------------------- #

G_CHOICES = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Third Gender"),)

D_CHOICES = (
    ("1", "----------"),
    ("2", "Cardiology"),
    ("3", "Neurology"),
    ("4", "Orthopedics"),
    ("5", "Dermatology"),
    ("6", "Nephronology"),
    ("7", "Gynacologist"),
)
HOSPITALS_LIST_CHOICES = (
    ("1", "ABC"),
    ("2", "DEF"),
    ("3", "GHI"),
    ("4", "JKL"),
    ("5", "MNO"),
    ("6", "PQR"),
    ("7", "STU"),
)


class NameWidget(forms.MultiWidget):
    def __init__(self, attrs = None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        if value:
            return value.split(" ")
        return [" ", " "]


class NameField(forms.MultiValueField):
    widget = NameWidget

    def __init__(self, *args, **kwargs):
        fields = {
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a Valid First Name (Only Letters)')
            ]),
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a Valid Second Name (Only Letters)')
            ])
        }

        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return f'{data_list[0]}{data_list[1]}'


class appointment(forms.Form):
    # name = forms.CharField(max_length=100, label="Name")
    name = NameField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=G_CHOICES)
    age = forms.CharField()
    phone_number = forms.CharField()
    email_id = forms.EmailField(max_length=250)
    country = CountryField().formfield()
    # hospitals = forms.ChoiceField(choices=HOSPITALS_LIST_CHOICES)
    department = forms.ChoiceField(choices=D_CHOICES)
    reports = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'POST'

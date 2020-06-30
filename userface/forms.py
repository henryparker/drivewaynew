from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userface.models import Vehicle
from userface.models import ParkingSpot
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField
    last_name = forms.CharField

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class VehicleForm(forms.Form):
    make = forms.CharField(label="Make", required=True)
    model = forms.CharField(label="Model", required=True)
    #color = forms.CharField(label="Color", required=True)

    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

    class Meta:
        model = Vehicle
        fields = ["make", "model"]

class ParkingSpaceForm(forms.Form):
    address = forms.CharField(label="Address", required=True)
    city = forms.CharField(label="City", required=True)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

    class Meta:
        model = ParkingSpot
        fields = ["address", "city"]
from typing import OrderedDict
from .models import Order, Customer, Product
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model =Order
        fields ='__all__'
class CustomerForm(ModelForm):
    
    class Meta:
        model =Customer
        fields ='__all__'

class CreatUserForm(UserCreationForm):
    class Meta:
        model =User
        fields =['first_name','last_name','username','email','password1','password2']



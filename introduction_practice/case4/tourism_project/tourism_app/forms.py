# tourism_app/forms.py

from django import forms
from .models import Tour, Service, Client, Operator, Order

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['tour_name', 'tour_description', 'duration', 'price']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description', 'price']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ['operator_name', 'contact_info']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'tour', 'operator', 'order_date', 'total_price']

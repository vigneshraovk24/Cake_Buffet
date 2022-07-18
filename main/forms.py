from django import forms

class OrderDetailsForm(forms.Form):
    alt_name = forms.CharField(max_length=50)
    alt_phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=400)
    Order_instructions = forms.CharField(max_length=200)
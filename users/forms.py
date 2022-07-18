from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Customer

class NewUSerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = Customer
        fields = ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2","address")

    def save(self,commit=True):
        user = super(NewUSerForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.address = self.cleaned_data["address"]
        if commit:
            user.save()
        return user
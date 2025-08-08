from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_money', 'Mobile Money'),
    ]
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.Select(), required=True)
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'postal_code']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

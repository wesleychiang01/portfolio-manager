# forms.py
from django import forms
from .models import Holding

class HoldingForm(forms.ModelForm):
    class Meta:
        model = Holding
        fields = ['company', 'trade_date', 'quantity', 'unit_per_share', 'brokerage']

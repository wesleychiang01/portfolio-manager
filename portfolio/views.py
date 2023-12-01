from django.shortcuts import render, redirect
from .forms import HoldingForm
from .models import Holding

# Create your views here.

def portfolio(request):
    holdings = Holding.objects.all()
    print(holdings)
    return render(request, 'portfolio/index.html', {'holdings': holdings})

def portfolio_add(request):
    return render(request, 'portfolio/portfolio_add.html')

def enter_holding_details(request):
    holdings = Holding.objects.all()
    
    if request.method == 'POST':
        company = request.POST.get('company')
        trade_date = request.POST.get('trade_date')
        quantity = request.POST.get('quantity')
        unit_per_share = request.POST.get('unit_per_share')
        brokerage = request.POST.get('brokerage')

        holding = Holding(company=company, trade_date=trade_date, quantity=quantity, unit_per_share=unit_per_share, brokerage=brokerage)
        holding.save()

        return render(request, 'portfolio/index.html', {'holdings': holdings})
    
    return render(request, 'portfolio/portfolio_add.html')
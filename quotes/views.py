from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import requests
import json
# Create your views here.

def search_stock(base_url, stock_ticker):
    try:
        token = settings.IEXCLOUD_TEST_API_TOKEN
        url = base_url + stock_ticker + '?token=' + token
        data = requests.get(url)
        print(data)

        if data.status_code == 200:
            data = json.loads(data.content)
        else:
            data = {'Error' : 'There was a problem with your provided ticker symbol. Please try again'}
    except Exception as e:
        data = {'Error':'There has been some connection error. Please try again later.'}
    return data

def home(request):
    if request.method == 'POST':
        stock_ticker = request.POST['stock_ticker']
        base_url = 'https://api.iex.cloud/v1/data/core/quote/'
        stocks = search_stock(base_url, stock_ticker)
        return render(request, 'quotes/index.html', {'stocks':stocks})
    return render(request, 'quotes/index.html')
 
def welcome(request):
    return render(request, 'quotes/welcome.html')
 

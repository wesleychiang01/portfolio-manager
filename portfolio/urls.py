from django.urls import path

from . import views

urlpatterns = [
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio_add', views.portfolio_add, name='portfolio_add'),
    path('enter_stock', views.enter_holding_details, name='enter_holding_details'),
]
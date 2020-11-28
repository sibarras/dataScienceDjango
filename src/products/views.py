from django.shortcuts import render
from .models import Product
import pandas as pd
# Create your views here.

def chart_select_view(request):
    qs = Product.objects.all().values()
    
    return render(request, 'products/main.html', {})
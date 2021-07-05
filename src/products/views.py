from django.shortcuts import render
from .models import Product
import pandas as pd
# Create your views here.


def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    print(product_df)
    return render(request, 'products/main.html', {})
from django.shortcuts import render
from .models import Porfolio

# Create your views here.
def portfolio(request):
    portfolios = Porfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})
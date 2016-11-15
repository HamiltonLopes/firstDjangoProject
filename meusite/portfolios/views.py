from django.shortcuts import render
# import portfolios.templates.portfolios
# Create your views here.
def portfolio_exibir(request):
	return render(request, 'portfolios/portfolio_exivir.html', {})
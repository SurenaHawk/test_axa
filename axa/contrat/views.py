from django.shortcuts import render
from .forms import RisqueForm
# Create your views here.

def home(request):
    return render(request, 'contrat/home.html')

def devis(request):
    form = RisqueForm()
    # if request.method == 'POST':
    #     form = RisqueForm(request.POST)
    #     if form.is_valid():
    #         print("okkkk")
    # else:
    #     form = RisqueForm()
    return render(request, 'contrat/devis.html', {'form': form})
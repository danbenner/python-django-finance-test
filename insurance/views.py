from django.shortcuts import render
from django.http import HttpResponse

def insurance(request):
  return render(request, 'insurance/insurance.html')

from django.shortcuts import render
from django.http import HttpResponse

def debt(request):
  return render(request, 'debt/debt.html')

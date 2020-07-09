from django.shortcuts import render
from django.http import HttpResponse

def savings(request):
  return render(request, 'savings/savings.html')

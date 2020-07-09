from django.shortcuts import render
from django.http import HttpResponse

def spending(request):
  return render(request, 'spending/spending.html')

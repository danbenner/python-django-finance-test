from django.shortcuts import render
from django.http import HttpResponse

def taxes(request):
  return render(request, 'taxes/taxes.html')

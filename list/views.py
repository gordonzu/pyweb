#######################################
# views.py
# gordon Zuehlke 3-11-20
#######################################

from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')




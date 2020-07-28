from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import os
from datetime import datetime
from datetime import date

# Create your views here.

def backpack(request):
    return render(request,'backpack/backpack.html',{'nbar':'backpack'})


class Scraper:
    def __init__(self):
        pass

from django.shortcuts import render
from django.http import HttpResponse
import requests
from json2html import *


def tabet(request):
    basic = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false").json
    extra = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json
    # return HttpResponse(r)
    return render(request,'index.html',{'result':basic,'extra':extra})


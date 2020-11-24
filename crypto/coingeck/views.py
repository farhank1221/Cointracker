from django.shortcuts import render
from django.http import HttpResponse
import requests
from json2html import *


def tabet(request):
    url = 'https://api.coingecko.com/api/'
    endpoint = 'v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    extra = requests.get(url+endpoint).json
    # return HttpResponse(r)
    return render(request,'index.html',{'extra':extra})


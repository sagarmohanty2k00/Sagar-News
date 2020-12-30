from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
import requests

# Create your views here

key = 'Enter Your API Key Here'

def index(request):
    req = f'http://newsapi.org/v2/everything?q=latest&from=2020-11-30&sortBy=publishedAt&apiKey={key}'
    resp = requests.get(req)
    data = resp.json()

    constraints = {
        'title': 'Latest News',
        'data': data["articles"],
    }

    return render(request, 'index.html', constraints)


def search(request):
    query = request.GET.get("search")
    req = f'http://newsapi.org/v2/everything?q={query}&from=2020-11-30&sortBy=publishedAt&apiKey={key}'
    resp = requests.get(req)
    data = resp.json()

    constraints = {
        'title': 'Latest News',
        'data': data["articles"],
    }
    return render(request, 'index.html', constraints)

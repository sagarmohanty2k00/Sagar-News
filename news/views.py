from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
import requests

# Create your views here
headers = {
    'x-rapidapi-host': "google-news1.p.rapidapi.com",
    'x-rapidapi-key': "5fb7c103f9msh9ebeb81d68d6d5fp194942jsn5f0327cc0d41"
}

def index(request):
    url = "https://google-news1.p.rapidapi.com/top-headlines"

    querystring = {"country":"US", "lang":"en", "limit":"50"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    constraints = {
        'title': 'Latest News',
        'data': response["articles"],
    }


    return render(request, 'index.html', constraints)


def search(request):
    query = request.GET.get("search")
    url = "https://google-news1.p.rapidapi.com/search"

    querystring = {"q":query ,"country":"US", "lang":"en", "source":"cnn.com", "limit":"50", "when":"30d"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    constraints = {
        'title': query,
        'data': response["articles"],
    }


    return render(request, 'index.html', constraints)

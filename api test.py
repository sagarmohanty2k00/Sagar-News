import requests

url = "https://google-news1.p.rapidapi.com/top-headlines"

querystring = {"country":"US","lang":"en","limit":"50"}

headers = {
    'x-rapidapi-host': "google-news1.p.rapidapi.com",
    'x-rapidapi-key': "5fb7c103f9msh9ebeb81d68d6d5fp194942jsn5f0327cc0d41"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
import requests

# Create your views here
headers = {
    'x-rapidapi-host': "google-news1.p.rapidapi.com",
    'x-rapidapi-key': "KEY HERE"
}

response = {"statusCode":200,"articles":[{"title":"Powerful earthquake strikes southwest Mexico - CNN","link":"https://www.cnn.com/2021/09/07/americas/mexico-earthquake/index.html","source":{"title":"CNN","url":"https://www.cnn.com"},"published_date":"2021-09-08T04:28:00+00:00"},

{"title":"Biden heckled in New Jersey for stranding Americans in Afghanistan: 'He will leave you behind' - Fox News","link":"https://www.foxnews.com/politics/biden-heckled-new-jersey-americans-afghanistan","source":{"title":"Fox News","url":"https://www.foxnews.com"},"published_date":"2021-09-07T19:56:31+00:00"},

{"title":"Biden's Speech on Climate Change and Ida: Full Transcript - The New York Times","link":"https://www.nytimes.com/2021/09/07/us/politics/biden-speech-transcript-hurricane-ida.html","source":{"title":"The New York Times","url":"https://www.nytimes.com"},"published_date":"2021-09-07T22:56:46+00:00"},

{"title":"Afghanistan's new interior minister heads a US-designated terror group - Business Insider","link":"https://www.businessinsider.com/afghanistan-new-interior-minister-heads-a-us-designated-terror-group-2021-9","source":{"title":"Business Insider","url":"https://www.businessinsider.com"},"published_date":"2021-09-07T17:36:57+00:00"},

{"title":"Chaos and confusion: The frenzied final hours of the Afghan government - BBC News","link":"https://www.bbc.com/news/world-asia-58477131","source":{"title":"BBC News","url":"https://www.bbc.com"},"published_date":"2021-09-08T00:42:55+00:00"},{"title":"Alleged 9/11 plotters, including Khalid Sheikh Mohammed, appear at Guantanamo pretrial hearing - CNN","link":"https://www.cnn.com/2021/09/07/politics/alleged-9-11-plotters-trial-day-1/index.html","source":{"title":"CNN","url":"https://www.cnn.com"},"published_date":"2021-09-07T21:56:00+00:00"},{"title":"Alexandria Ocasio-Cortez slams Texas GOP governor's 'deep ignorance' on abortion - CNN","link":"https://www.cnn.com/2021/09/07/politics/aoc-texas-abortion-law-greg-abbott-cnntv/index.html","source":{"title":"CNN","url":"https://www.cnn.com"},"published_date":"2021-09-08T04:25:00+00:00"},{"title":"Biden Asks Congress For $30 Billion To Help Disaster Relief And Afghan Evacuees - NPR","link":"https://www.npr.org/2021/09/07/1034923509/biden-asks-congress-for-30-billion-to-help-disaster-relief-and-afghan-evacuees","source":{"title":"NPR","url":"https://www.npr.org"},"published_date":"2021-09-07T21:42:34+00:00"},{"title":"Fighting continues in Afghanistan's Panjshir Valley as anti-Taliban resistance vows to hold out - CNBC","link":"https://www.cnbc.com/2021/09/07/afghanistan-update-anti-taliban-resistance-vows-to-hold-out-in-panjshir-valley.html","source":{"title":"CNBC","url":"https://www.cnbc.com"},"published_date":"2021-09-07T18:53:44+00:00"},{"title":"State revokes nursing home licenses for owner who sent 800 residents to warehouse for Ida - NOLA.com","link":"https://www.nola.com/news/healthcare_hospitals/article_c0e3fe6c-1001-11ec-904b-838ad8570726.html","source":{"title":"NOLA.com","url":"https://www.nola.com"},"published_date":"2021-09-07T20:39:00+00:00"}]}

def index(request):
    url = "https://google-news1.p.rapidapi.com/top-headlines"

    querystring = {"country":"US", "lang":"en", "limit":"50"}

    # response = requests.request("GET", url, headers=headers, params=querystring)
    constraints = {
        'title': 'Latest News',
        'data': response,
    }


    return render(request, 'index.html', constraints)


def search(request):
    query = request.GET.get("search")
    url = "https://google-news1.p.rapidapi.com/search"

    querystring = {"q":query ,"country":"US", "lang":"en", "source":"cnn.com", "limit":"50", "when":"30d"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    constraints = {
        'title': query,
        'data': response,
    }


    return render(request, 'index.html', constraints)

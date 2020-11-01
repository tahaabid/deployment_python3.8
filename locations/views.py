from django.shortcuts import render
from django.views.generic import TemplateView
#import requests
# Create your views here.

def search_location(request):
    resultstring = location = ""
    if request.method == "POST":
        location = request.POST.get('geodata_search')
        PARAMS = {'q':location}
        URL = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch"
        response = requests.get(url=URL,params=PARAMS).json()
        resultstring = response[0]["nameEN"]
    context = {
        'loc': resultstring
    }
    return render(request, "locations.html", context)

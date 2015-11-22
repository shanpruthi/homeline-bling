"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *;
from django.shortcuts import render_to_response
from twilio.twiml import Response
from .forms import Shelter_Form

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

def shelter_information(request):
    shelter_information = Shelter_Information.objects.all();
    return render_to_response('app/database.html', {'shelter_information': shelter_information})

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

import json, requests



######## Helper Functions ############


def geocoding(location):
    return "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyA7XxD_9Z_7uJpi5Jx0sXFe_dT3NL2qpCk"

def get_user_location(location):
    reqSent = requests.post(geocoding(location))
    jsonSent = json.loads(reqSent.content)
    latitude = jsonSent['results'][0]['geometry']['location']['lat']
    longitude = jsonSent['results'][0]['geometry']['location']['lng']

    return {'latitude': latitude, 'longitude': longitude}

def get_closest_shelter(location):
    shelters = Shelter_Information.objects.filter(spots_remaining__gt=0).values('longitude', 'latitude', 'shelter_name', 'shelter_address')
    current_location = get_user_location(location)

    closest_name = ""
    closest_address = ""

    shortest = 10000
    for key in shelters:
        length = sqrt(pow(shelters[key].latitude-current_location['latitude'],2) + pow(shelters[key].longitude - current_location['longitude'],2))
        if length < shortest:
            closest_name = shelters[key].shelter_name
            closest_address = shelters[key].shelter_address

    return [closest_name, closest_address]


######## View Functions ##############

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'message':'',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
def shelters(request):
    """Renders the shelters page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/shelters.html',
        context_instance = RequestContext(request,
        {
            'title':'Shelters',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def database(request):
    """Renders the database page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/database.html',
        context_instance = RequestContext(request,
        {
            'title':'Database',
            'message':'Your database page.',
            'year':datetime.now().year,
        })
    )
    resultant = Shelter_Information.objects.all()
    if request.method == "GET":
        form = Shelter_Form();
        return render(request, 'app/database.html', {'form': Shelter_Form})
    elif request.method == "POST":
        form = Shelter_Form(request.POST)
        form.save()
        return HttpResponseRedirect('/home')

def login(request):
    """Renders the login page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        context_instance = RequestContext(request,
        {
            'title':'Login',
            'message':'Log in to your account.',
            'year':datetime.now().year,
        })
    )
@twilio_view
def gather_digits(request):
    twilio_response = Response()
    city = request.POST.get('FromCity', '')
    
    #shelter = get_closest_shelter(city)
    twilio_response.say("Hello")

    return twilio_response
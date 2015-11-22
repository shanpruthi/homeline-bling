"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *;
from django.shortcuts import render_to_response
<<<<<<< HEAD
#from twilio.twiml import Response
from .forms import Shelter_Form

#from django_twilio.decorators import twilio_view
#from twilio.twiml import Response

def shelter_information(request):
    shelter_information = Shelter_Information.objects.all();
    return render_to_response('app/database.html', {'shelter_information': shelter_information})
=======

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

import json, requests

######## Helper Functions ############

def geocoding(location):
    return "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyA7XxD_9Z_7uJpi5Jx0sXFe_dT3NL2qpCk"

def get_closest_shelter(location):
    reqSent = requests.post(geocoding(location))
    jsonSent = json.loads(reqSent.content)
    latitude = jsonSent['results'][0]['geometry']['location']['lat']
    longitude = jsonSent['results'][0]['geometry']['location']['lng']

    return {'latitude': latitude, 'longitude': longitude}

######## View Functions ##############
>>>>>>> 6bac01ac29fbfd6df35a45e703b64ba55fc0a0c9

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
'''
@twilio_view
def gather_digits(request):
    twilio_response = Response()
    city = request.POST.get('FromCity', '')
    shelters = Shelter_Information.objects.filter(spots_remaining__gt=0)
    shelter = get_closest_shelter(city)
    twilio_response.say("You are from %s" % shelter)

    return twilio_response
<<<<<<< HEAD

@twilio_view
def handle_response(request):
    digits = request.POST.get('Digits', '')
    twilio_response = Response()
    if digits == '1':
        twilio_response.say("Hah, you don't get a song")
 
    if digits == '2':
        number = request.POST.get('From', '')
        twilio_response.say('A text message is on its way')
        twilio_response.sms('Hello!', to="+14167006502")
 
    return twilio_response

'''
=======
>>>>>>> 6bac01ac29fbfd6df35a45e703b64ba55fc0a0c9

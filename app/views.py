"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
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

@twilio_view
def gather_digits(request):
    twilio_response = Response()
 
    with twilio_response.gather(action='/respond/', numDigits=1) as g:
        g.say('Press one to be dissapointed, two to receive an SMS')
        g.pause(length=1)
        g.say('Press one to be dissapointed, two to receive an SMS')
 
    return twilio_response

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
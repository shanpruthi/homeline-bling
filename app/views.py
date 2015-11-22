"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
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

def gather_digits(request):
    twilio_response = Response()
 
    with twilio_response.gather(action='/respond/', numDigits=1) as g:
        g.say('Press one to hear a song, two to receive an SMS')
        g.pause(length=1)
        g.say('Press one to hear a song, two to receive an SMS')
 
    return twilio_response
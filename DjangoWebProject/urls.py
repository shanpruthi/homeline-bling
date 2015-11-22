"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^shelterinfo$', 'app.views.shelter_information', name='shelterinfo'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
<<<<<<< HEAD
    url(r'^database', 'app.views.database', name='database'),
=======
    url(r'^shelters', 'app.views.shelters', name='shelters'),
>>>>>>> 6bac01ac29fbfd6df35a45e703b64ba55fc0a0c9
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
<<<<<<< HEAD
 #   url(r'^gather/$', 'app.views.gather_digits'),
  #  url(r'^respond/$', 'app.views.handle_response'),
=======
    url(r'^gather/$', 'app.views.gather_digits'),
>>>>>>> 6bac01ac29fbfd6df35a45e703b64ba55fc0a0c9
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

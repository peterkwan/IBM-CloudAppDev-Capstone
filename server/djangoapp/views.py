from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarDealer, DealerReview
# from .restapis import related methods
from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        template_name = request.POST['template_name']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(template_name)
        else:
            context['message'] = 'Invalid user name and/or password'
            context['template_name'] = template_name
            return render(request, 'djangoapp/login.html', context)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        context['template_name'] = request.META['HTTP_REFERER']
        return render(request, 'djangoapp/registration.html', context)
    else:
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['pwd']
        email = request.POST['email']
        template_name = request.POST['template_name']

        try:
            User.objects.get(username=username)
            context['message'] = 'User already exists'
            context['template_name'] = template_name
            return render(request, 'djangoapp/registration.html', context)
        except:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            login(request, user)
            return redirect(template_name)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == 'GET':
        url = 'https://6133d11d.us-south.apigw.appdomain.cloud/api/dealership'
        dealerships = get_dealers_from_cf(url, **(request.GET))
        context['dealerships'] = dealerships
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == 'GET':
        url = 'https://6133d11d.us-south.apigw.appdomain.cloud/api/review'
        dealer_reviews = get_dealer_reviews_from_cf(url, dealer_id)
        dealer_review_names = '<br/>'.join([review.name + ' - Review: ' + review.sentiment for review in dealer_reviews])
        return HttpResponse(dealer_review_names)

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def add_review(request, review):
    pass


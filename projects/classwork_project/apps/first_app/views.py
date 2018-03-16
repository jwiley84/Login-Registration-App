from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
	response = "Hello world! I am your first request. This is the function portion of flask's app routing!"
	return HttpResponse(response)

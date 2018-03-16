from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    text = "Did this really work? probably not."
    return HttpResponse(text)

def new(request):
    text = 'Is this a placeholder for new blogs?'
    return HttpResponse(text)

def create(request):
    return redirect('/')

def show(request, number):
    text = "Sweet lord of the oceans, Elder God of complete destruction..."
    num = "The number is " + str(number)
    return HttpResponse(text, num)

def edit(request, number):
    text = "MmmmHmmm"
    num = "The number is " + str(number)
    return HttpResponse(text, num)

def destroy(request, number):
    return redirect('/')
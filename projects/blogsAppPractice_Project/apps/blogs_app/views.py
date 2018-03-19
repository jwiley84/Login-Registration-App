from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    text = "Did this really work? probably not."
    return HttpResponse(text)

def new(request):
    text = 'Is this a placeholder for new blogs?'
    return HttpResponse(text)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect('/')

def show(request, number):
    text = "Sweet lord of the oceans, Elder God of complete destruction..."
    #num = "The number is " + str(number)
    return HttpResponse(text)

def edit(request, number):
    text = "MmmmHmmm"
    #num = "The number is " + str(number)
    return HttpResponse(text)

def destroy(request, number):
    return redirect('/')
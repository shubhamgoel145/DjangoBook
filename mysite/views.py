from django.http import HttpResponse

def home(request):
    return HttpResponse("Shubham's Django Journey")

def hello(request):
    return HttpResponse("Hello World")

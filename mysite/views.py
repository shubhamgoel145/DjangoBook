from django.http import HttpResponse
import datetime

def home(request):
    return HttpResponse("Shubham's Django Journey")

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "The current date-time is %s" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "The Time in %s hour(s), it will be %s" % (offset, dt)
    return HttpResponse(html)

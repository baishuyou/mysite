from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
 #   html = t.render({'current_date': now})
 #   return HttpResponse(html)


#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    c = {'current_date': now}
#    html = t.render(c)
#    return HttpResponse(html)

def current_datetime(request):
    current_date = datetime.datetime.now()
    #return render(request,'current_datetime.html', locals())
    return render_to_response('current_datetime.html', locals())
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
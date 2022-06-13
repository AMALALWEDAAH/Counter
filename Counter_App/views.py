from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")



def visitnumber(request):
    visitnumber=request.session.get('visitnumber',0)
    request.session['visitnumber'] += 1
    context={
        'visitnumber':visitnumber,
    }


    return render(request, 'index.html', context=context)

def destroySession (request):
    try:
        del request.session['visitnumber']
    except  KeyError:
        pass
    return redirect ('/')


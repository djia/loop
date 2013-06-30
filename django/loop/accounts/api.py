from accounts.models import *
from interests.models import *
from events.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse

connect('suloop')

def get_eventusers(request):
	#get all users going to this event
	eventid = request.GET.get('eventid')
	eventuserlist = EventUser.objects.filter(event=eventid)
	return HttpResponse(eventuserlist.to_json(), content_type="application/json")

def get_interestusers(request):
	#get all users going to this event
	interestid = request.GET.get('interestid')
	interestuserlist = InterestUser.objects.filter(interest=interestid)
	return HttpResponse(interestuserlist.to_json(), content_type="application/json")


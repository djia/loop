from accounts.models import *
from interests.models import *
from events.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse

connect('suloop')


def get_events_nearme(request):
	#function to get nearby events,
	#currently get all events (no location)
	gpsx = request.GET.get('gpsx')
	gpsy = request.GET.get('gpsy')
	return HttpResponse(Event.objects.to_json(), content_type="application/json")

def get_events_nearme_ofmyinterest(request):
	gpsx = request.GET.get('gpsx')
	gpsy = request.GET.get('gpsy')
	userid = request.Get.get('userid')
	interestuserlist = InterestUser.objects.filter(user=userid)
	interestlist = []
	for iu in interestuserlist:
		interestlist.append(iu.interest)
	eventlist = InterestEvent.objects.filter(interest__in = interestlist)
	return HttpResponse(eventlist.to_json(), content_type="application/json")


def get_eventmessages(request):	
	#get posts by all users for a given
	#event
	eventid = request.GET.get('eventid')
	eventmessagelist = EventMessage.objects.filter(event=eventid)
	return HttpResponse(eventmessagelist.to_json(), content_type="application/json")


def get_myevents(request):
	#get the events that this user is
	#going to
	userid = request.GET.get('userid')
	return_list = []
	myeventlist = EventUser.objects.filter(user=userid)
	return HttpResponse(myeventlist.to_json(), content_type="application/json")

def get_interestevents_nearme(request):
	gpsx = request.GET.get('gpsx')
	gpsy = request.GET.get('gpsy')
	interestid = request.Get.get('interestid')
	eventlist = InterestEvent.objects.filter(interest=interestid)
	return HttpResponse(eventlist.to_json(), content_type="application/json")
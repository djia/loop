from accounts.models import *
from interests.models import *
from events.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse

connect('suloop')


def getEventsNearMe(userid):
	#function to get nearby events,
	#currently get all events (no location)
	return HttpResponse(Event.objects.to_json(), content_type="application/json")



def getInterestCategories(self):
	#function to get all interest categories
	#later this will also be geolocalized
	json = InterestCategory.objects.to_json()
	return HttpResponse(json, content_type="application/json")


def getInterestCategoryInterests(request):
	#function to get all interests of a
	#given interestcategory
	#later this will also be geo
	ic = request.GET.get('interestcategoryid')
	return_list = []
	interestcategory = InterestCategory.objects.with_id(ic)
	print interestcategory.name
	for interest in Interest.objects:
		if interest.interestcategory.pk == interestcategory.pk:
			print interest.name
			return_list.append(interest.to_json())

	return HttpResponse(return_list, content_type="application/json")



def getEventMessages(eventid):	
	#get posts by all users for a given
	#event
	event = Event.objects.with_id(eventid)
	return HttpResponse(event.eventmessages.to_json(), content_type="application/json")



def getEventUsers(eventid):
	#get all users going to this event
	event = Event.objects.with_id(eventid)
	return HttpResponse(event.users.to_json(), content_type="application/json")


"""
def getMyInterests(userid):
	#get user's interests, ones he has 
	#subscribed to
	return_list = []
	user = User.objects.with_id(userid)
	for interest in Interest.objects(users__in=[user]:
		return_list.append(interest)

	return return_list

def getMyEvents(userid):
	#get the events that this user is
	#going to
	return_list = []
	user = User.objects.with_id(userid)
	for event in Event.objects(users__in=[user]):
		return_list.append(event)

	return return_list
"""
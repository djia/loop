from accounts.models import *
from interests.models import *
from events.models import *



def getEventsNearMe(userid):
	#function to get nearby events,
	#currently get all events (no location)
	return Event.objects



def getInterestCategories():
	#function to get all interest categories
	#later this will also be geolocalized
	return InterestCategory.objects


def getInterestCategoryInterests(interestcategoryid):
	#function to get all interests of a
	#given interestcategory
	#later this will also be geo
	return_list = []
	interestcategory = InterestCategory.objects.with_id(interestcategoryid)
	for interest in Interest.objects:
		if interest.interestcategory == interestcategory:
			return_list.append(interest)

	return return_list



def getEventMessages(eventid):	
	#get posts by all users for a given
	#event
	event = Event.objects.with_id(eventid)
	return event.eventmessages



def getEventUsers(eventid):
	#get all users going to this event
	event = Event.objects.with_id(eventid)
	return event.users



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




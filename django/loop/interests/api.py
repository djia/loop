from accounts.models import *
from interests.models import *
from events.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse

connect('suloop')


def get_interestcategories(request):
	#function to get all interest categories
	#later this will also be geolocalized
	#gpsx = request.GET.get('gpsx')
	#gpsy = request.GET.get('gpsy')
	json = InterestCategory.objects.to_json()
	return HttpResponse(json, content_type="application/json")


def get_interestcategory_interests_nearme(request):
	#function to get all interests of a
	#given interestcategory
	#later this will also be geo
	gpsx = request.GET.get('gpsx')
	gpsy = request.GET.get('gpsy')
	interestcategoryid = request.GET.get('interestcategoryid')
	interestlist = Interest.objects.filter(interestcategory=interestcategoryid)
	return HttpResponse(interestlist.to_json(), content_type="application/json")


def get_myinterests(request):
	#get user's interests, ones he has 
	#subscribed to
	userid = request.GET.get('userid')
	interestlist = InterestUser.objects.filter(user=userid)
	return HttpResponse(interestlist.to_json(), content_type="application/json")

def get_eventinterests(request):
	eventid = request.GET.get('eventid')
	interestlist = InterestEvent.objects.filter(event=eventid)
	return HttpResponse(interestlist.to_json(), content_type="application/json")
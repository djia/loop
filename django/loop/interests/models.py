from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField
from events.models import Event
from accounts.models import User

class InterestCategory(Document):
	name = StringField(max_length=50, required=True)
	time_created = DateTimeField()
	time_updated = DateTimeField()


class Interest(Document):
	name = StringField(max_length=200, required=True)
	interestcategory = ReferenceField(InterestCategory, reverse_delete_rule=CASCADE)
	time_created = DateTimeField()
	time_updated = DateTimeField()


class InterestEvent(Document):
	interest = ReferenceField(Interest)
	event = ReferenceField(Event)
	time_created = DateTimeField()
	time_updated = DateTimeField()


class InterestUser(Document):
	interest = ReferenceField(Interest)
	user = ReferenceField(User)
	time_created = DateTimeField()
	time_updated = DateTimeField()

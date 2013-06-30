from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField
from accounts.models import User

class Event(Document):
	name = StringField(required=True)
	venue = StringField()
	time = DateTimeField()
	description = StringField()
	time_created = DateTimeField()
	time_updated = DateTimeField()

class EventUser(Document):
	event = ReferenceField(Event)
	user = ReferenceField(User)
	time_created = DateTimeField()
	time_updated = DateTimeField()

class EventMessage(Document):
	message = StringField()
	user = ReferenceField(User)
	event = ReferenceField(Event)
	time_created = DateTimeField()
	time_updated = DateTimeField()

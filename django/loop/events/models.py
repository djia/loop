from mongoengine import *
from django.db import models
from django.core.urlresolvers import reverse
from djangotoolbox.fields import ListField, EmbeddedModelField
from accounts.models import User

class EventMessage(EmbeddedDocument):
	#object_id = IntField(primary_key=True)
	message = StringField()
	user = ReferenceField(User)
	date_time_stamp = DateTimeField()

class Event(Document):
	#object_id = IntField(primary_key=True)
	name = StringField(required=True)
	venue = StringField()
	time = DateTimeField()
	description = StringField()
	users = ListField(ReferenceField(User, reverse_delete_rule=NULLIFY))
	eventmessages = ListField(EmbeddedDocumentField(EventMessage))
	date_time_stamp = DateTimeField()
from mongoengine import *
from django.db import models
from django.core.urlresolvers import reverse
from djangotoolbox.fields import ListField, EmbeddedModelField
from accounts.models import User
from events.models import Event

class InterestCategory(Document):
	#object_id = IntField(primary_key=True)
	name = StringField(max_length=50, required=True)
	date_time_stamp = DateTimeField()

class Interest(Document):
	#object_tid = IntField(primary_key=True)
	name = StringField(max_length=200, required=True)
	interestcategory = ReferenceField(InterestCategory, reverse_delete_rule=CASCADE)
	users = ListField(ReferenceField(User))
	date_time_stamp = DateTimeField()



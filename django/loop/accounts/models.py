from mongoengine import *
from django.db import models
from django.core.urlresolvers import reverse
from djangotoolbox.fields import ListField, EmbeddedModelField

class User(Document):
	#object_id = IntField(primary_key=True)
	email = EmailField(required=True)
	first_name = StringField(max_length=50)
	last_name = StringField(max_length=50)
	address = StringField(max_length=100)
	date_time_stamp = DateTimeField()
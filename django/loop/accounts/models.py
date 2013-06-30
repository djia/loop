from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField

class User(Document):
	email = EmailField(required=True)
	first_name = StringField(max_length=50)
	last_name = StringField(max_length=50)
	address = StringField(max_length=100)
	time_created = DateTimeField()
	time_updated = DateTimeField()
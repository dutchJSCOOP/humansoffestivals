from django.db import models
from django.contrib.auth.models import User

# Create your models here. HUMANSOFFESTIVALS

class Post(models.Model):
	text = models.TextField()
	facebookLink = models.TextField()
	postID = models.TextField()
	festivalName = models.TextField()
	festivalDate(DD-MM-YY) = models.TextField()
	poster = models.TextField()
	date_time = models.DateTimeField(auto_now=True)
	photo = models.ImageField(null=True, blank =True)
	identifiers = models.TextField()
	def __str__(self):
		return self.postID

class CalendarItem(models.Model):
	text = models.Textfield()
	facebookLink = models.TextField()
	date(DD-MM) = models.models.TextField()
	def __str__(self):
		return self.text
		

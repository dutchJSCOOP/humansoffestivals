from django.db import models
from django.contrib.auth.models import User
import datetime  
# Create your models here. HUMANSOFFESTIVALS

class Post(models.Model):
	text = models.TextField()
	facebookLink = models.TextField()
	postID = models.TextField()
	festivalName = models.TextField()
	festivalDate = models.DateField( default=datetime.date.today)
	poster = models.TextField()
	photo = models.ImageField(null=True, blank =True)
	identifiers = models.TextField()
	def __str__(self):
		return self.postID

class CalendarItem(models.Model):
	festivalName = models.TextField()
	facebookLink = models.TextField()
	festivalDate= models.DateField( default=datetime.date.today)
	def __str__(self):
		return self.festivalName
		

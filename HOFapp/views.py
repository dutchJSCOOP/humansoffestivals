from django.shortcuts import render
from HOFapp.models import Post, CalendarItem
# Create your views here. HUMANSOFFESTIVALS

def index(request):
	posts = Post.objects.all().order_by('-festivalDate')
	calendarItems = CalendarItem.objects.all().order_by('festivalDate')
	return render(request, 'HOFapp/index.html', {'posts':posts, 'calendarItems':calendarItems})
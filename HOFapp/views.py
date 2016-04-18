from django.shortcuts import render
from HOFapp.models import Post
# Create your views here. HUMANSOFFESTIVALS

def index(request):
	posts = Post.objects.all()
	return render(request, 'HOFapp/index.html', {'posts':posts})
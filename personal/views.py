from django.shortcuts import render
from operator import attrgetter

from news.models import NewsPost



def home_screen_view(request):
	
	context = {}
	news_posts = sorted(NewsPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
	context['news_posts'] = news_posts

	return render(request, "personal/home.html", context)
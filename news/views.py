from django.shortcuts import render, redirect, get_object_or_404

from news.models import NewsPost
from news.forms import CreateNewsPostForm, UpdateNewsPostForm
from account.models import Account


def create_news_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateNewsPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=request.user.email).first()
		obj.author = author
		obj.save()
		form = CreateNewsPostForm()

	context['form'] = form

	return render(request, 'news/create_news.html', context)



def detail_news_view(request, slug):

	context = {}
	news_post = get_object_or_404(NewsPost, slug=slug)
	context['news_post'] = news_post

	return render(request, 'news/detail_news.html', context)




def edit_news_view(request, slug):
	
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	news_post = get_object_or_404(NewsPost, slug=slug)
	if request.POST:
		form = UpdateNewsPostForm(request.POST or None, request.FILES or None, instance=news_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			news_post = obj
	
	form = UpdateNewsPostForm(
			initial={
					"title": news_post.title, 
					"body": news_post.body,
					"image": news_post.image,
				}
			)
	context['form'] = form

	return render(request, 'news/edit_news.html', context)
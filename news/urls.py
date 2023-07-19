from django.urls import path
from news.views import (
	create_news_view,
	detail_news_view,
	edit_news_view,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_news_view, name="create"),
    path('<slug>/', detail_news_view, name="detail"),
    path('<slug>/edit/', edit_news_view, name="edit"),
 ]
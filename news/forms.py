from django import forms

from news.models import NewsPost 


class CreateNewsPostForm(forms.ModelForm):

	class Meta:
		model = NewsPost
		fields = ['title', 'body', 'image']


class UpdateNewsPostForm(forms.ModelForm):

	class Meta:
		model = NewsPost
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		news_post = self.instance
		news_post.title = self.cleaned_data['title']
		news_post.body = self.cleaned_data['body']
		# News_post.published = self.cleaned_data['published']

		if self.cleaned_data['image']:
			news_post.image = self.cleaned_data['image']

		if commit:
			news_post.save()
		return news_post
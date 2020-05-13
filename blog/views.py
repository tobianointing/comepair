from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView, 
	CreateView, 
	UpdateView,
	DeleteView
	)
# Create your views here.

class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/blog/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False		



# def author_post(request, id):

# 	posts = Post.objects.all().filter(author_id=id)

# 	context = {
# 		'posts': posts
# 	}

# 	return render(request, 'blog/author_posts.html', context)




class AuthorPostListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/author_posts.html'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))

		return Post.objects.filter(author=user).order_by('-date_posted')

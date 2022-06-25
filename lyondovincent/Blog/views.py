from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostBaseView(View):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('films:all')

class PostListView(PostBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all Film objects"""

class PostDetailView(PostBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class PostCreateView(PostBaseView, CreateView):
    """View to create a new film"""

class PostUpdateView(PostBaseView, UpdateView):
    """View to update a film"""

class PostDeleteView(PostBaseView, DeleteView):
    """View to delete a film"""
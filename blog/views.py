from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
# posts = [
#     {
#         'author':'Tashi Wangchuk',
#         'title':'Know about chenla',
#         'content':'We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value.The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method.We can also use the del keyword to remove individual items or the entire dictionary itself.',
#         'date_posted':'Janurary 01, 2019'
#     },
#
#     {
#         'author': 'Sonam Dorji',
#         'title': 'Why visit chenla',
#         'content':'We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value.The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method.We can also use the del keyword to remove individual items or the entire dictionary itself.',
#         'date_posted': 'Janurary 02, 2019'
#     },
# ]
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    # context is the dictonary which is a collection of unordered and changable index
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#class base views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'#<app>/<model>_<viewtype>.hmtl------>blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'#<app>/<model>_<viewtype>.hmtl------>blog/post_list.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title':'About'})



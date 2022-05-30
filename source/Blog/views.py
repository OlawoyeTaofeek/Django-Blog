from re import template
from django.shortcuts import get_object_or_404, render, reverse
from Blog.models import Post
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # """newest to oldest"""
    paginate_by = 5
    

class UserPostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'Blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # """newest to oldest"""
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author= user).order_by('-date_posted')

"""In summary, **kwargs is dict that holds parameters and can be used by first passing it through a view func e.g

def fun(req, **kwargs)

and then get values inside the function like this

kwargs.get('key_name')."""

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
    
    
"""Verify that the current user is authenticated. If not redirect to the login page before you can post"""
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
"""Verify that the current user is authenticated. If not redirect to the login page before you can post"""
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'Blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'Blog/post_delete.html'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
    def get_success_url(self):
        return reverse('blog-home')
    
    # OR
    #success_url = '/'

















    
    
    
    
    
    
    
    
    
    
    
    
    
    

    # making the author current user rather than adding or choosing new one
    #def form_valid(self, form):
     #   form.instance.author =  self.request.user
      #  return super().form_valid(form)
   


def about(request):
    return render(request, 'about.html', {'title':'about'})


#Class Based Views
#<app>/<model>_<viewtype>.html
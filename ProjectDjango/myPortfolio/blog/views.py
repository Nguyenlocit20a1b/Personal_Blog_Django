
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.

    
class PostListView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    ordering =["-date"]
# detail 
class PostDetail( DetailView):
    model = Post 
    template_name = 'post_detail.html'
    context_object_name = 'post'

    
# creat Post
def PostCreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Create Succsessfully for {title}')
            return redirect('blog-home')
    else:
        form = BlogForm()
    return render(request, 'createPost.html',{'form':form})

#update Post
class PostUpdate (LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    success_url ='/blog'
    fields = ['title', 'body' , 'blog_img']
    template_name = 'post_update.html'
    
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

#delete Post 
class  PostDelete (LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name ='post_confirm_delete.html'
    success_url ='/blog'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
            
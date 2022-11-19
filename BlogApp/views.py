from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from BlogApp.models import Blog, Comment,Likes
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from BlogApp.forms import CommentForm
import uuid




# Create your views here.


class CratBlogView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'BlogApp/creat_blog.html'
    fields = ('title','blog_content','blog_img',)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        title = obj.title
        obj.slug = title.replace("","-") + "-" + str(uuid.uuid4())
        obj.save()
        return HttpResponseRedirect(reverse('index'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'BlogApp/blog_list.html'

@login_required
def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    alrady_like = Likes.objects.filter(blog=blog, user=request.user)
    if alrady_like:
        likes = True
    else:
        likes = False
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blogapp:blog_detail' , kwargs={'slug':slug}))
            
    return render(request, 'BlogApp/detail_blog.html', context={'blog':blog, 'form':comment_form, 'likes':likes,})
    
    
@login_required
def Liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    alrady_like = Likes.objects.filter(blog=blog, user=user)
    if not alrady_like:
        likepost = Likes(blog=blog, user=user)
        likepost.save()
    return HttpResponseRedirect(reverse('blogapp:blog_detail', kwargs={'slug':blog.slug}))

@login_required
def Unlike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    alrady_like = Likes.objects.filter(blog=blog, user=user)
    alrady_like.delete()
    return HttpResponseRedirect(reverse('blogapp:blog_detail', kwargs={'slug':blog.slug}))


class my_blog(LoginRequiredMixin,TemplateView):
    template_name= 'BlogApp/my_blog.html'

class UdateBlogs(LoginRequiredMixin, UpdateView):
    model= Blog
    fields=('title','blog_content','blog_img')
    template_name= 'BlogApp/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blogapp:blog_detail' , kwargs={'slug':self.object.slug})

class DeleteBlogs(LoginRequiredMixin, DeleteView):
    context_object_name ='blog'
    model = Blog
    success_url = reverse_lazy('blogapp:my_blog')
    template_name = 'BlogApp/delete_blog.html'
    



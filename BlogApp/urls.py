from django.urls import path
from . import views

app_name = 'blogapp'


urlpatterns = [
    path('',views.BlogList.as_view() , name='blogs'),
    path('CreateBlog/',views.CratBlogView.as_view(), name='CreateBlog'),
    path('blog_detail/<slug>', views.blog_detail,name='blog_detail'),
    path('Liked/<pk>/', views.Liked, name='Liked'),
    path('unLiked/<pk>/', views.Unlike, name='Unlike'),
    path('myblog/', views.my_blog.as_view(), name='my_blog'),
    path('UdateBlogs/<pk>/', views.UdateBlogs.as_view(), name='UdateBlogs'),
    path('DeleteBlogs/<pk>/', views.DeleteBlogs.as_view(), name='DeleteBlogs'),

    
    
]

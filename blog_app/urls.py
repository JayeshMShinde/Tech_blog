# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.blogHome, name = "bloghome"),
#     # path('postcomment', views.postComment, name="postComment"),
#     path('postComment', views.postComment, name='postComment'),
#     path('post-a-blog', views.blogadd, name = "add_blog"),
#     path('<int:pk>', views.bloghome_view, name='bloghome_view'),
#     path('<str:slug>', views.blogPost, name="blogPost"),
#     path('like/<int:pk>/',views.liked_post, name="liked_post")
# ]
# 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('postComment', views.postComment, name='postComment'),
    path('post-a-blog', views.blogadd, name="add_blog"),
    path('<int:pk>', views.bloghome_view, name='bloghome_view'),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('like/<int:pk>/', views.liked_post, name="liked_post")
]
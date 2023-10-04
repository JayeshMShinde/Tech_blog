    # """
    # The above code is a collection of functions for a blog application in Django, including functions
    # for displaying the blog home page, individual blog posts, posting comments, adding new blog posts,
    # and viewing a specific blog post.
    
    # :param request: The request object, which contains information about the current HTTP request
    # :return: The code is returning different things depending on the view function being called:
    # """
from django.shortcuts import render, HttpResponse, redirect
from blog_app.models import Post, BlogComment
from .forms import BlogPostForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from blog_app.templatetags import extras
from django.urls import reverse
import json

def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")


def blogadd(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('bloghome')
    else:
        form = BlogPostForm()
    return render(request, 'blog/Addpost.html', {'form': form})


def bloghome_view(request, pk):
    post = get_object_or_404(Post, sno=pk)
    liked_count = post.like_User.count()    
    context = {'post': post, 'liked_count': liked_count}
    print("context : ", context['post'].title )
    return render(request, 'blog/bloghome.html', context)   


@login_required
def liked_post(request, pk):
    post = get_object_or_404(Post, sno=pk)
    if(request.user not in post.like_User.all()):
        post.like_User.add(request.user)
        post.save()
        messages.success(request ,"you liked a Post")

    liked_count = post.like_User.count()
    return JsonResponse(liked_count, safe=False)

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, sno=pk)

    # Check if the user is the author of the blog post
    if request.user != post.author:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        messages.success(request, "Your post has been updated successfully.")
        return redirect('post_detail', pk=pk)

    context = {'post': post}
    return render(request, 'blog/blogpost.html', context)

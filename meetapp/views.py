import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import Post, Comment

def post_home(request):
    post_home = Post.objects.all()
    concert_list = Concert.objects.all()
    context = {
        'post_home': post_home,
        'concert_list' : concert_list,
    }
    return render(request, 'meetapp/post_home.html', context)

def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'meetapp/post_list.html', context)

@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.likes_user.filter(id=user.id).exists():
        post.likes_user.remove(user)
    else:
        post.likes_user.add(user)

    context = {'likes_count':post.count_likes_user()}
    return HttpResponse(json.dumps(context), content_type="application/json")


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post.hit +=1
    post.save()
    context = {
            'post': post
        }
    return render(request, 'meetapp/post_detail.html', context)

def post_resethit(request,post_id):
    post = Post.objects.get(id=post_id)
    post.views = 0
    post.save()
    return render(request, 'meetapp/post_detail.html')

def post_new(request):
    if request.method == 'GET':
        #빈 폼 보여주는 부분
        form = PostForm()

    elif request.method == 'POST':
        # 사용자가 입력한 데이터를 저장하는 부분
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #post.id 없음
            post.user = request.user 
            post.save() #post.id 저장
            return redirect('meetapp:post_detail', post_id=post.id)

    return render(request, 'meetapp/post_new.html', {
        'form': form,
    })
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)

    elif request.method == 'POST':
        # 사용자가 입력한 데이터를 저장하는 부분
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.hit -= 1 
            post = form.save()
            return redirect('meetapp:post_detail', post_id=post.id)

    return render(request, 'meetapp/post_edit.html', {
        'form': form,
        'post': post,
    })

def post_delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, blog_id=post_id)
    post.delete()
    return redirect('meetapp:post_list')

@login_required
def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('meetapp:post_detail',post.id)
    else:
        form = CommentForm() 
    return render(request, 'meetapp/comment_form.html', {
        'form' : form,
    })

@login_required
def comment_edit(request, post_id,id):
    comment = get_object_or_404(Comment,id=id)
    if comment.user != request.user:
        return redirect('meetapp:post_detail', post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            comment.save()
            return redirect('meetapp:post_detail',post_id)
    else:
        form = CommentForm(instance=comment) 
    return render(request, 'meetapp/comment_form.html', {
        'form' : form,
    })

@login_required
def comment_delete(request, post_id,id):
    comment = get_object_or_404(Comment,id=id)
    if comment.user != request.user:
        return redirect('meetapp:post_detail', post_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('meetapp:post_detail', post_id)
    
    return render(request, 'meetapp/comment_confirm_delete.html', {
        'comment' : comment,
    })

def content_list(request):
    concert_list = Concert.objects.all()
    context = {
        'concert_list' : concert_list,
    }
    return render(request, 'meetapp/content_list.html', context)
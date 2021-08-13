import json
from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.paginator import EmptyPage, Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .forms import *
from .models import Post, Comment, PostDeclaration, CommentDeclaration


def post_home(request):
    hit_posts = Post.objects.all().order_by('-hit')[:10]
    concert_list = Concert.objects.all()
    context = {
        'posts': hit_posts,
        'concert_list': concert_list,
    }
    return render(request, 'meetapp/post_home.html', context)


def search_result(request):
    page = request.GET.get("page", 1)
    keyword = request.GET.get('keyword')
    results = Post.objects.filter(
        Q(title__icontains=keyword) | Q(content__icontains=keyword))
    paginator = Paginator(results, 10, orphans=3)
    try:
        lists = paginator.page(int(page))
    except EmptyPage:
        return redirect("/")
    context = {
        'searchstr': keyword,
        'posts': results,
        'page': lists,
    }
    return render(request, 'meetapp/search_result.html', context)


def post_list(request):
    page = request.GET.get("page", 1)
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10, orphans=3)
    try:
        lists = paginator.page(int(page))
        return render(request, "meetapp/post_list.html", {
            "page": lists
        })
    except EmptyPage:
        return redirect("/")


@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = UserInfo.objects.get(userkey=request.user)

    if post.likes_user.filter(id=user.id).exists():
        post.likes_user.remove(user)
    else:
        post.likes_user.add(user)

    context = {'likes_count': post.count_likes_user()}
    return HttpResponse(json.dumps(context), content_type="application/json")


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post.hit += 1
    post.save()
    form = CommentForm()
    if post.pcp.pcp_user.filter(id=request.user.id).exists():
        is_pcp = 1
    else:
        is_pcp = 0

    context = {
        'post': post,
        'form': form,
        'is_pcp': is_pcp,
    }
    return render(request, 'meetapp/post_detail.html', context)


def post_resethit(request, post_id):
    post = Post.objects.get(id=post_id)
    post.views = 0
    post.save()
    return render(request, 'meetapp/post_detail.html')


def post_new(request):
    if request.method == 'GET':
        form = PostForm()

    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = UserInfo.objects.get(userkey=request.user)
            pcp = Participant.objects.create(created_user=post.user)
            try:
                max_pcp = request.POST.get('max_pcp')
                pcp.pcp_user_total = max_pcp
            except:
                pass
            pcp.save()
            post.pcp = pcp
            post.save()
            return redirect('meetapp:post_detail', post_id=post.id)

    return render(request, 'meetapp/post_new.html', {
        'form': form,
    })


def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.hit -= 1
            try:
                max_pcp = request.POST.get('max_pcp')
                post.pcp.pcp_user_total = max_pcp
                post.pcp.save()
            except:
                pass
            post = form.save()
            return redirect('meetapp:post_detail', post_id=post.id)

    return render(request, 'meetapp/post_edit.html', {
        'form': form,
        'post': post,
    })


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.pcp.delete()
    post.delete()
    return redirect('meetapp:post_list')


@login_required
def post_declaration(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        form = PostDeclareForm()

    elif request.method == 'POST':
        form = PostDeclareForm(request.POST)
        if form.is_valid():
            declaration = form.save(commit=False)
            declaration.user = post.user
            declaration.post = post
            declaration.save()
            postdeclaration = form.save(commit=False)
            postdeclaration.user = post.user
            postdeclaration.post = post
            postdeclaration.save()
            return redirect('meetapp:post_detail', post_id=post.id)
    return render(request, 'meetapp/post_declaration.html', {
        'form': form,
    })


@login_required
def comment_declaration(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'GET':
        form = CommentDeclareForm()

    elif request.method == 'POST':
        form = CommentDeclareForm(request.POST)
        if form.is_valid():
            commentdeclaration = form.save(commit=False)
            commentdeclaration.user = comment.user
            commentdeclaration.post = post
            commentdeclaration.comment = comment
            commentdeclaration.save()
            return redirect('meetapp:post_detail', post_id=post.id)

    return render(request, 'meetapp/comment_declaration.html', {
        'form': form,
    })


@login_required
def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = UserInfo.objects.get(userkey=request.user)
            comment.save()
            return redirect('meetapp:post_detail', post.id)
    return redirect('meetapp:post_detail', post.id)


@login_required
def comment_edit(request, post_id, id):
    comment = get_object_or_404(Comment, id=id)
    if comment.user.username != request.user.username:
        return redirect('meetapp:post_detail', post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            comment.save()
            return redirect('meetapp:post_detail', post_id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'meetapp/comment_form.html', {
        'form': form,
    })


@login_required
def comment_delete(request, post_id, id):
    comment = get_object_or_404(Comment, id=id)
    if comment.user.username != request.user.username:
        return redirect('meetapp:post_detail', post_id)
    comment.delete()
    return redirect('meetapp:post_detail', post_id)


def pcp_add(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if post.pcp.pcp_user.filter(id=comment.user.userkey.id).exists():
        context = {'status': 0}
    else:
        post.pcp.pcp_user.add(comment.user)
        post.pcp.pcp_user_count += 1
        post.pcp.save()
        post.save()
        add_user = UserInfo.objects.get(username=comment.user.username)
        print(add_user.concertnum)
        add_user.concertnum += 1
        add_user.save()
        context = {'status': 1, 'pcp_user_count': post.pcp.pcp_user_count}

    return HttpResponse(json.dumps(context), content_type="application/json")


def pcp_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if post.pcp.pcp_user.filter(id=comment.user.userkey.id).exists():
        post.pcp.pcp_user.remove(comment.user)
        post.pcp.pcp_user_count -= 1
        post.pcp.save()
        post.save()
        del_user = UserInfo.objects.get(username=comment.user.username)
        del_user.concertnum -= 1
        if del_user.concertnum < 0:
            del_user.concertnum = 0
        del_user.save()
        context = {'status': 1, 'pcp_user_count': post.pcp.pcp_user_count}
    else:
        context = {'status': 0}

    return HttpResponse(json.dumps(context), content_type="application/json")


def content_list(request):
    concert_list = Concert.objects.all()
    context = {
        'concert_list': concert_list,
    }
    return render(request, 'meetapp/content_list.html', context)

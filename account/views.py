from django.db.models.fields.related import ForeignObject
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.db.models import Q
import json
from .forms import *
from . import models


def user(request, user_id):
    print("request user:" + request.user.username)
    users = User.objects.get(username=user_id)
    infos = UserInfo.objects.get(username=user_id)
    try:
        reviews = Review.objects.filter(tguser_id=user_id)
    except Review.DoesNotExist:
        reviews = ""
    age = infos.get_age()

    if request.user.username != user_id:
        if request.user.username:
            try:
                following = Follow.objects.get(
                    follow_user_id=request.user.username, followed_user_id=user_id)
                if following:
                    isFollowed = 2
                else:
                    isFollowed = 3
            except:
                isFollowed = 3
        else:
            isFollowed = 3
    else:
        isFollowed = -1

    if infos.interests:
        infos.interests = json.loads(infos.interests)

    context = {
        'info': infos,
        'age': age,
        'reviews': reviews,
        'isFollowed': isFollowed,
        'users': users,
    }
    return render(request, 'account/user.html', context)


def user_edit(request, user_id):
    print(request.POST)

    info = UserInfo.objects.get(username=user_id)
    if request.method == 'POST':
        infoForm = UserInfoForm(request.POST, instance=info)
        infoForm.gender = request.POST.get('gender')
        tempinterests = request.POST.getlist('interests')
        M = dict(zip(tempinterests, range(1, len(tempinterests) + 1)))

        if infoForm.is_valid():
            info = infoForm.save(commit=False)
            info.interests = json.dumps(M)
            info.save()
            return redirect('account:user', user_id)
        else:
            print("invalid")
    else:
        infoForm = UserInfoForm(instance=info)
    return render(request, 'account/user_edit.html', {'user_id': user_id, 'infoform': infoForm, 'cur_info': info})


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'meetapp/post_home.html')


def sign(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        infoForm = UserJoinForm(request.POST, request.FILES)
        infoForm.gender = request.POST.get('gender')
        tempinterests = request.POST.getlist('interests')
        M = dict(zip(tempinterests, range(1, len(tempinterests) + 1)))

        if form.is_valid() and infoForm.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            new_user = infoForm.save(commit=False)
            new_user.username = username
            new_user.userkey = user
            new_user.gender = infoForm.gender
            new_user.interests = json.dumps(M)
            new_user.save()
            user = authenticate(username=username, password=raw_password)
            return redirect('account:login')
        else:
            print("validation failed")
    else:
        form = UserForm()
        infoForm = UserJoinForm()
    return render(request, 'account/sign.html', {'form': form, 'infoform': infoForm})


def follow(request, user_id):
    try:
        user = UserInfo.objects.get(username=request.user.username)
        tguser = UserInfo.objects.get(username=user_id)
    except UserInfo.DoesNotExist:
        return redirect('account:user', user_id)
    user.following += 1
    tguser.follower += 1
    user.save()
    tguser.save()

    following = Follow.objects.create(follow_user_id=user.username, follow_user_username=user.name,
    followed_user_id=tguser.username, followed_user_username=tguser.name)
    following.save()
    return redirect('account:user', user_id)


def unfollow(request, user_id):
    userID = request.user.username
    if not userID:
        return redirect('account:user', user_id)

    try:
        user = UserInfo.objects.get(username=userID)
        tguser = UserInfo.objects.get(username=user_id)
    except UserInfo.DoesNotExist:
        return redirect('account:user', user_id)
    user.following -= 1
    tguser.follower -= 1
    if user.following < 0:
        user.following = 0
    if tguser.follower < 0:
        tguser.follower = 0
    user.save()
    tguser.save()

    unfollowing = Follow.objects.get(
        follow_user_id=userID, followed_user_id=user_id)
    unfollowing.delete()

    return redirect('account:user', user_id)


def follow_list(request, user_id):
    order = request.GET.get("order")
    print(order)
    follow = Follow.objects.filter(Q(followed_user_id=user_id) & Q(follow_user_id=user_id))
    if(order == "follower"):
        follow = Follow.objects.filter(followed_user_id=user_id)
    elif(order == "following"):
        follow = Follow.objects.filter(follow_user_id=user_id)
    else:
        redirect("/")

    return render(request, 'account/follow_list.html', {
        "tguser_id":user_id,
        "order":order,
        "follow": follow,
    })


def review_new(request, user_id):
    userinfo = get_object_or_404(UserInfo, username=request.user.username)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = request.user.username
            review.user_info = userinfo
            review.tguser_id = user_id
            review.save()
            return redirect('account:user', user_id)
    else:
        form = ReviewForm()
    return render(request, 'account/review_form.html', {
        'form': form,
    })


def review_edit(request, user_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return redirect('account:user', user_id)

    if review.user_id != request.user.username:
        return redirect('account:user', user_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            review.save()
            return redirect('account:user', user_id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'account/review_form.html', {
        'form': form,
    })


def review_delete(request, user_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return redirect('account:user', user_id)

    if review.user_id == request.user.username:
        review.delete()
    return redirect('account:user', user_id)

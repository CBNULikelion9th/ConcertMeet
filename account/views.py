from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

# Create your views here.

def user(request, user_id):
    users = User.objects.get(username=user_id)
    infos = UserInfo.objects.get(username=user_id)
    try:
        reviews = Review.objects.filter(tguser_id=user_id)
    except Review.DoesNotExist:
        reviews=""
    age = infos.get_age()

    if request.user.username != user_id:
        try:
            following = Follow.objects.get(follow_user_id=request.user.username, followed_user_id=user_id)
            if following:
                isFollowed = 2
            else:
                isFollowed = 3
        except:
            isFollowed = 3
    else:
        isFollowed = -1


    context = {
            'req_user':request.user.username,
            'user': users,
            'info': infos,
            'age':age,
            'reviews': reviews,
            'isFollowed': isFollowed
        }
    return render(request, 'account/user.html', context)

def user_edit(request, user_id):
    user = User.objects.get(username=user_id)
    info = UserInfo.objects.get(username=user_id)
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=user)
        infoForm = UserInfoForm(request.POST, request.FILES, instance=info)
        if userForm.is_valid() and infoForm.is_valid():
            userForm.save()
            infoForm.save()
            return redirect('user', user_id)
    else:
        userForm = UserForm(instance=user)
        infoForm = UserInfoForm(instance=info)
    return render(request, 'account/user_edit.html', { 'user':userForm, 'info':infoForm })

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'meetapp/post_home.html')

def sign(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        infoForm = UserInfoForm(request.POST, request.FILES)
        interestForm = request.POST.get_list("interest")
        if form.is_valid() and infoForm.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            infoForm.interest = interestForm
            infoForm.save(commit=False)
            infoForm.username=username
            infoForm.save()
            user = authenticate(username = username, password = raw_password)
            return redirect('account:login')
    else:
        form = UserForm()
        infoForm = UserInfoForm()
    return render(request, 'account/sign.html', {'form': form, 'infoform': infoForm })

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

    following = Follow.objects.create(follow_user_id=request.user.username, followed_user_id=user_id)
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

    unfollowing = Follow.objects.get(follow_user_id=userID, followed_user_id=user_id)
    unfollowing.delete()

    return redirect('account:user', user_id)

def review_new(request, user_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = request.user.username
            review.tguser_id = user_id
            review.save()
            return redirect('account:user', user_id)
    else:
        form = ReviewForm() 
    return render(request, 'account/review_form.html', {
        'form' : form,
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
        'form' : form,
    })

def review_delete(request, user_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return redirect('account:user', user_id)

    if review.user_id == request.user.username:
        review.delete()
    return redirect('account:user', user_id)
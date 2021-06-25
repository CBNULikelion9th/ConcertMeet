from django.shortcuts import render, redirect
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
    context = {
            'user': users,
            'info': infos,
            'age':age,
            'reviews': reviews
        }
    return render(request, 'account/user.html', context)

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'meetapp/post_home.html')

def sign(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        infoForm = UserInfoForm(request.POST, request.FILES)
        if form.is_valid() and infoForm.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            infoForm.save(commit=False)
            infoForm.username=username
            infoForm.save()
            user = authenticate(username = username, password = raw_password)
            return redirect('account:login')
    else:
        form = UserForm()
        infoForm = UserInfoForm()
    return render(request, 'account/sign.html', {'form': form, 'infoform': infoForm })


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

def review_edit(request, review_id):
    review = get_object_or_404(Review,id=review_id)
    if review.user.id != request.user.id:
        return redirect('meetapp:user')
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            review.save()
            return redirect('meetapp:user')
    else:
        form = ReviewForm(instance=review) 
    return render(request, 'meetapp/review_form.html', {
        'form' : form,
    })

def review_delete(request, review_id):
    review = get_object_or_404(Review,id=review_id)
    if review.user != request.user:
        return redirect('meetapp:user')
    if request.method == 'POST':
        review.delete()
        return redirect('meetapp:user')
    
    return render(request, 'meetapp/review_confirm_delete.html', {
        'review' : review,
    })
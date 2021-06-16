from django.urls import path
from . import views

app_name='meetapp'

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('lists/', views.post_list, name='post_list'),
    path('lists/<int:post_id>/', views.post_detail, name='post_detail'),
    path('lists/new/', views.post_new, name='post_new'),
    path('lists/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('lists/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('lists/<int:post_id>/user/', views.post_user, name='post_user'),
    path('login/', views.login, name='login'),
    path('sign/', views.sign, name='sign'),
    path('lists/<int:post_id>/comment/new/', views.comment_new, name='comment_new'),
    path('lists/<int:post_id>/comment/<int:id>/edit/', views.comment_edit, name='comment_edit'),
    path('lists/<int:post_id>/comment/<int:id>/delete/', views.comment_delete, name='comment_delete'),
    path('lists/<int:post_id>/review/new/', views.review_new, name='review_new'),
    path('lists/<int:post_id>/review/<int:id>/edit/', views.review_edit, name='review_edit'),
    path('lists/<int:post_id>/review/<int:id>/delete/', views.review_delete, name='review_delete'),
]
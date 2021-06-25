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
    
    path('lists/<int:post_id>/comment/new/', views.comment_new, name='comment_new'),
    path('lists/<int:post_id>/comment/<int:id>/edit/', views.comment_edit, name='comment_edit'),
    path('lists/<int:post_id>/comment/<int:id>/delete/', views.comment_delete, name='comment_delete'),
]
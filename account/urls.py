from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign/', views.sign, name='sign'),
    path('<user_id>/', views.user, name='user'),
    path('<user_id>/edit', views.user_edit, name='user_edit'),

    path('<user_id>/follow/', views.follow, name='follow'),
    path('<user_id>/unfollow/', views.unfollow, name='unfollow'),
    path('<user_id>/follow_list', views.follow_list, name='follow_list'),

    path('<user_id>/review/new/', views.review_new, name='review_new'),
    path('<user_id>/review/<int:review_id>/edit/',
         views.review_edit, name='review_edit'),
    path('<user_id>/review/<int:review_id>/delete/',
         views.review_delete, name='review_delete'),
]

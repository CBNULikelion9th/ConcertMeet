from django.db import models
from django.urls.base import reverse
import django.utils.timezone as timezone
from django.conf import settings


class UserInfo(models.Model):
    userkey = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=5, null=True)
    interests = models.JSONField(default=list, null=True, blank=True)
    profpic = models.ImageField(
        null=True, blank=True, upload_to='user/profilepic')
    introduction = models.TextField(blank=True)
    following = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)
    concertnum = models.IntegerField(default=0)
    # concert participation. 참가한 공연 목록이며 데이터는 게시글의 id가 들어감
    concertpcp = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_age(self):
        return timezone.now().year - self.date_of_birth.year + 1


class Follow(models.Model):
    follow_user_id = models.CharField(max_length=30)
    follow_user_username = models.CharField(max_length=100)
    followed_user_id = models.CharField(max_length=30)
    followed_user_username = models.CharField(max_length=100)

    def __str__(self):
        return f'팔로우: {self.follow_user_id}'


class Review(models.Model):
    user_id = models.CharField(max_length=30)
    user_info = models.ForeignKey('UserInfo', on_delete=models.CASCADE,)
    tguser_id = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

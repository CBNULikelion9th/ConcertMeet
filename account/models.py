from django.db import models
from django.urls.base import reverse
import django.utils.timezone as timezone
from django.conf import settings

class UserInfo(models.Model):
    username=models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=30)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    gender_choice = (('남자', '남자'), ('여자', '여자'))
    gender = models.CharField(max_length=10, choices=gender_choice, null=True)
    interests = models.JSONField(null=True)

    profpic = models.ImageField(blank=True, upload_to='user/profilepic')
    introduction = models.TextField(blank=True)
    following = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)
    concertnum = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_age(self):
        return timezone.now().year - self.date_of_birth.year + 1

class Follow(models.Model):
    follow_user_id = models.CharField(max_length=30)
    followed_user_id = models.CharField(max_length=30)

class Review(models.Model):
    user_id = models.CharField(max_length=30)
    tguser_id = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
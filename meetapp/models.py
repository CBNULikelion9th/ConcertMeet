from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    hit = models.IntegerField(default=-1)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes_user') 
    pcp = models.ForeignKey('Participant',on_delete=models.CASCADE)
    
    def count_likes_user(self): 
        return self.likes_user.count()

    def __str__(self):
        return f'{self.title}'

class Participant(models.Model):
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pcp_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='pcp_user')  #공연 참가 유저수. 사용자가 존재하면 글 삭제 불가능. 유저 아이디 넣기

    pcp_user_count = models.IntegerField(default=1)
    pcp_user_total = models.IntegerField(default=4)

    def count_pcp_user(self):
        pcp_user_count += 1
        return self.pcp_user.count()

    def decount_pcp_user(self):
        pcp_user_count -= 1
        return self.pcp_user.count()
        
    def __str__(self):
        return f'{self.id}'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def get_edit_url(self):
        return reverse('meetapp:comment_edit', args=[self.post.id, self.id])
    
    def get_delete_url(self):
        return reverse('meetapp:comment_delete', args=[self.post.id, self.id])

class Declaration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    message = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    process = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.message}'


class Concert(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField('url', unique=True)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'

# class Photo(models.Model):
#     post = models.ForeignKey(Concert, on_delete=models.CASCADE, null=True)
    
from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE,)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def get_edit_url(self):
        return reverse('meetapp:comment_edit', args=[self.post.id, self.id])
    
    def get_delete_url(self):
        return reverse('meetapp:comment_delete', args=[self.post.id, self.id])

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE,)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def get_edit_url(self):
        return reverse('meetapp:review_edit', args=[self.post.id, self.id])
    
    def get_delete_url(self):
        return reverse('meetapp:review_delete', args=[self.post.id, self.id])


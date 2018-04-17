from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(to=User, related_name='liked', through="Like")

    def __str__(self):
        return str(self.author) + '/' + self.text


    @property
    def total_likes(self):
        return self.liked.count()


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)

    def __str__(self):
        return '#' + str(self.post.pk) + '(' + str(self.post.text) + (') liked by ' if self.like else ') disliked by ') + self.liker.username

    class Meta:
        unique_together = (("liker", "post"),)

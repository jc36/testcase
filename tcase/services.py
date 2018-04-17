from django.contrib.auth import get_user_model
from tcase.models import Like, Post

User = get_user_model()


def create_post(author, text):
    p = Post(text=text, author=author)
    p.save()
    return p.pk


def show_post(post):
    return Post.objects.filter(pk=post)


def show_posts_all():
    return Post.objects


def rem_post(post):
    Post.objects.filter(pk=post).delete()


def add_like(liker, post):
    """like post"""
    like, is_created = Like.objects.get_or_create(liker=liker, post=post)
    return like


def remove_like(liker, post):
    """dislike"""
    Like.objects.filter(liker=liker, post=post).delete()


def is_fan(liker, post) -> bool:
    """check like"""
    # if not liker.is_authenticated:
    #     return False
    likes = Like.objects.filter(liker=liker, post=post)
    return likes.exists()


def get_fans(post):
    """get all likers"""
    return User.objects.filter(post=post)

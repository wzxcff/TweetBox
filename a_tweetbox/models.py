from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.TextField(validators=[MaxLengthValidator(280)])
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.text

class TweetImage(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="tweets/")

    def __str__(self):
        return f"Image for {self.tweet}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile avatar"
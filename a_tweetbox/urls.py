from django.urls import path

import TweetBox.settings
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("register/", register_view, name="register_view"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("feed/", feed_view, name="feed_view"),
    path("delete/<int:tweet_id>", delete_tweet, name="delete_tweet"),
    path("tweet/<int:tweet_id>/like/", like_tweet, name="like_tweet"),
]
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterForm, LoginForm, NewPostForm
from .models import Tweet, TweetImage


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("feed_view")
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate using email as the username
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)  # Log in the user
                return redirect('feed_view')  # Redirect to index
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = LoginForm()

    return render(request, "login.html", {'form': form})

@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    return redirect(index)

@login_required(login_url='login_view')
def feed_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            images = request.FILES.getlist('images')
            for image in images:
                TweetImage.objects.create(tweet=tweet, image=image)
            return redirect('feed_view')
    else:
        form = NewPostForm()
    tweets = Tweet.objects.all().order_by('-created_at')
    user = request.user
    return render(request, "main.html", {'form': form, 'tweets': tweets, 'user': user})

@login_required(login_url='login_view')
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if tweet.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this tweet.")

    tweet.delete()
    return redirect('feed_view')

@login_required(login_url='login_view')
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return redirect('feed_view')

@login_required(login_url='login_view')
def profile_view(request):
    return render(request, "profile.html")
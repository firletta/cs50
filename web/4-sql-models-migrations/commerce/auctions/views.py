from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.contrib.auth.decorators import login_required

from .models import User, Auction, Bid, Comment

def index(request):
    auctions = Auction.objects.all()
    return render(request, 'auctions/index.html', {'auctions': auctions})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        user = request.user
        image = request.POST["image"]
        auction = Auction(title=title, description=description, price=price, user=user, image=image)
        auction.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html")

def auction(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "price": auction.current_price(),
        "date": auction.created_at,
        "bids": auction.bids.all()
    })

@login_required
def comment(request, auction_id, user_id):
    auction = get_object_or_404(Auction, id=auction_id)
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        text = request.POST["text"]
        comment = Comment(text=text, user=user, auction=auction)
        comment.save()
        return HttpResponseRedirect(reverse("auction", args=(auction.id,)))
    else:
        return render(request, "auctions/auction.html", {'auction': auction, 'user': user})

@login_required
def bid(request, auction_id, user_id):
    auction = get_object_or_404(Auction, id=auction_id)
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        price = Decimal(request.POST["price"])
        if price <= auction.current_price():
            return render(request, "auctions/auction.html", {'auction': auction, 'user': user, "message": "Bid must be higher than current price."})
        bid = Bid(price=price, user=user, auction=auction)
        bid.save()
        return HttpResponseRedirect(reverse("auction", args=(auction.id,)))
    else:
        return render(request, "auctions/auction.html", {'auction': auction, 'user': user})

@login_required
def update_watchlist(request, auction_id, user_id):
    auction = get_object_or_404(Auction, id=auction_id)
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        if auction in user.watchlist.all():
            user.watchlist.remove(auction)
        else:
            user.watchlist.add(auction)
        return HttpResponseRedirect(reverse("auction", args=(auction.id,)))
    return render(request, "auctions/auction.html", {'auction': auction, 'user': user})

@login_required
def view_watchlist(request):
    user = request.user
    return render(request, "auctions/watchlist.html", {'user': user})

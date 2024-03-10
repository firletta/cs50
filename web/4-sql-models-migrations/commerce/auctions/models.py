from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Max
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    bids = models.ManyToManyField('Bid', blank=True, related_name="bidders")
    watchlist = models.ManyToManyField('Auction', blank=True, related_name="watchers")

    def __str__(self):
        return f"{self.username}"

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    active = models.BooleanField(default=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.current_price()}"

    def current_price(self):
        highest_bid = self.bids.aggregate(Max('price'))['price__max']
        return highest_bid if highest_bid is not None else self.price

class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey('Auction', on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")

    def __str__(self):
        return f"{self.user.username} bid {self.price} on {self.auction.title}"

    def __str__(self):
        return f"{self.user.username} bid {self.price} on {self.auction.title}"

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.text} - { self.user } - {self.auction.title}"

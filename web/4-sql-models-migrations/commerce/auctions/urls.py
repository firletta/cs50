from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("auction/<int:auction_id>", views.auction, name="auction"),
    path('comment/<int:auction_id>/<int:user_id>/', views.comment, name='comment'),
    path('bid/<int:auction_id>/<int:user_id>/', views.bid, name='bid'),
    path('watchlist/<int:auction_id>/<int:user_id>/', views.update_watchlist,
         name='update_watchlist'),
    path('watchlist/', views.view_watchlist, name='view_watchlist'),
]

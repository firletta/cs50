# Generated by Django 5.0.3 on 2024-03-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auction_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchers', to='auctions.auction'),
        ),
    ]

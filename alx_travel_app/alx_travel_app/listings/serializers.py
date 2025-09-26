from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_title', 'user', 'user_username', 'start_date', 'end_date', 'total_price', 'created_at']
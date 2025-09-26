from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from decimal import Decimal
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **options):
        # Create sample listings
        listings_data = [
            {
                'title': 'Cozy Beach House',
                'description': 'Beautiful beachfront property with stunning ocean views',
                'price_per_night': Decimal('150.00'),
                'location': 'Miami, FL'
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin in the mountains perfect for relaxation',
                'price_per_night': Decimal('120.00'),
                'location': 'Aspen, CO'
            },
            {
                'title': 'Downtown Loft',
                'description': 'Modern loft in the heart of the city',
                'price_per_night': Decimal('200.00'),
                'location': 'New York, NY'
            }
        ]

        for listing_data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults=listing_data
            )
            if created:
                self.stdout.write(f'Created listing: {listing.title}')

        # Create a sample user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'}
        )
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write('Created test user')

        # Create sample bookings
        listings = Listing.objects.all()[:2]
        for i, listing in enumerate(listings):
            start_date = date.today() + timedelta(days=30 + i*10)
            end_date = start_date + timedelta(days=3)
            total_price = listing.price_per_night * 3

            booking, created = Booking.objects.get_or_create(
                listing=listing,
                user=user,
                start_date=start_date,
                defaults={
                    'end_date': end_date,
                    'total_price': total_price
                }
            )
            if created:
                self.stdout.write(f'Created booking for: {listing.title}')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
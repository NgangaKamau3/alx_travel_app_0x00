# ALX Travel App 0x00

A Django-based travel booking application with listings, bookings, and reviews functionality.

## Models

- **Listing**: Travel property listings with title, description, price, and location
- **Booking**: User bookings for listings with date ranges and pricing
- **Review**: User reviews and ratings for listings

## Setup

1. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Seed the database with sample data:
```bash
python manage.py seed
```

## API Serializers

- **ListingSerializer**: Handles listing data serialization
- **BookingSerializer**: Handles booking data with related listing and user information
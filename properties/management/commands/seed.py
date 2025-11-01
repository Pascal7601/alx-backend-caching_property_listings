from properties.models import Property
from django.core.management.base import BaseCommand
from decimal import Decimal


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Seeding properties...')
        
        # 1. Clear existing data
        # We delete all old properties to start fresh.
        Property.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared old property data.'))

        # 2. Define sample data
        sample_properties = [
            {
                "title": "Sunny Beachfront Condo",
                "description": "A beautiful condo right on the beach. Perfect for a vacation getaway. Features 2 bedrooms, 2 baths, and a stunning ocean view.",
                "price": Decimal("350000.00"),
                "location": "Miami, FL"
            },
            {
                "title": "Cozy Mountain Cabin",
                "description": "Escape to the mountains in this rustic cabin. Features a wood-burning stove, 3 bedrooms, and is close to hiking trails.",
                "price": Decimal("210000.00"),
                "location": "Asheville, NC"
            },
            {
                "title": "Downtown Urban Loft",
                "description": "Modern loft in the heart of the city. Exposed brick, high ceilings, and walking distance to all restaurants and shops.",
                "price": Decimal("520000.00"),
                "location": "New York, NY"
            },
            {
                "title": "Quiet Suburban Home",
                "description": "A perfect family home in a quiet neighborhood. 4 bedrooms, 3 baths, a large backyard, and a 2-car garage. Close to great schools.",
                "price": Decimal("430000.00"),
                "location": "Austin, TX"
            },
            {
                "title": "Sprawling Country Estate",
                "description": "A massive estate on 10 acres of land. Features a private pool, guest house, and horse stables.",
                "price": Decimal("1250000.00"),
                "location": "Napa, CA"
            },
        ]

        # 3. Create properties in the database
        for data in sample_properties:
            # We use create() since we already deleted all objects
            prop = Property.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created property: "{prop.title}"'))

        self.stdout.write(self.style.SUCCESS('Seeding complete!'))

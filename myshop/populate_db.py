import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()

from store.models import Product

def populate():
    products = [
        {"name": "Kitenge Print Shirt", "price": 1500.00, "category": "Clothes", "image_url": "https://via.placeholder.com/200?text=Kitenge+Shirt"},
        {"name": "Kisii Highlands Fleece", "price": 2500.00, "category": "Clothes", "image_url": "https://via.placeholder.com/200?text=Fleece+Jacket"},
        {"name": "Classic Denim Jeans", "price": 1800.00, "category": "Clothes", "image_url": "https://via.placeholder.com/200?text=Denim+Jeans"},
        {"name": "Nairobi Streetwear Hoodie", "price": 2200.00, "category": "Clothes", "image_url": "https://via.placeholder.com/200?text=Streetwear+Hoodie"},
        {"name": "Official Cotton Trousers", "price": 1200.00, "category": "Clothes", "image_url": "https://via.placeholder.com/200?text=Cotton+Trousers"},
        {"name": "Leather Safari Boots", "price": 3500.00, "category": "Shoes", "image_url": "https://via.placeholder.com/200?text=Safari+Boots"},
        {"name": "Casual Canvas Sneakers", "price": 1000.00, "category": "Shoes", "image_url": "https://via.placeholder.com/200?text=Canvas+Sneakers"},
        {"name": "Open Toe Leather Sandals", "price": 800.00, "category": "Shoes", "image_url": "https://via.placeholder.com/200?text=Leather+Sandals"},
        {"name": "Running Athletics Shoes", "price": 2800.00, "category": "Shoes", "image_url": "https://via.placeholder.com/200?text=Running+Shoes"},
        {"name": "Formal Oxford Shoes", "price": 3000.00, "category": "Shoes", "image_url": "https://via.placeholder.com/200?text=Oxford+Shoes"},
    ]

    for p in products:
        obj, created = Product.objects.get_or_create(**p)
        if created:
            print(f"Added: {obj.name}")
        else:
            print(f"Already exists: {obj.name}")

if __name__ == '__main__':
    print("Populating the database with test products...")
    populate()
    print("Done!")
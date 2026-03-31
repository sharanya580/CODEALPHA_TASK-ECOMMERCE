import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Product
from django.core.files import File
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Dummy data
products = [
    {
        'name': 'Eclipse Noise-Cancelling Headphones',
        'price': 299.99,
        'description': 'Immerse yourself in pure sound with our active noise-cancelling technology. Premium comfort for all-day listening.',
        'image_path': 'static/images/product_headphones.png'
    },
    {
        'name': 'Nova Mechanical Keyboard',
        'price': 149.50,
        'description': 'Elevate your tech setup with our sleek, responsive mechanical keyboard featuring custom RGB underglow.',
        'image_path': 'static/images/product_keyboard.png'
    },
    {
        'name': 'Aero Ultra-Light Gaming Mouse',
        'price': 89.99,
        'description': 'Experience unparalleled precision with our ergonomic, high-performance gaming mouse.',
        'image_path': 'static/images/product_mouse.png'
    },
    {
        'name': 'Horizon Ultra-Wide Monitor',
        'price': 699.00,
        'description': 'See more of your work and play with this stunning ultra-wide curved display.',
        'image_path': 'static/images/product_monitor.png'
    }
]

import glob

print("Deleting old products...")
Product.objects.all().delete()

for p in products:
    # Find matching file since they have timestamps
    search_pattern = os.path.join(BASE_DIR, 'static/images', p['image_path'].split('/')[-1].replace('.png', '*.png'))
    matching_files = glob.glob(search_pattern)
    
    product, created = Product.objects.get_or_create(
        name=p['name'],
        defaults={
            'price': p['price'],
            'description': p['description']
        }
    )
    
    if matching_files:
        image_file = matching_files[0]
        with open(image_file, 'rb') as f:
            product.image.save(os.path.basename(image_file), File(f))
        product.save()

print("Products populated successfully.")

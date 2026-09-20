from django.shortcuts import render

PRODUCTS = [
    {
        'name': 'Heritage Leather Backpack',
        'description': 'Full-grain leather, padded laptop sleeve',
        'price': '128.00',
        'image': 'storefront/images/products/backpack.jpg',
    },
    {
        'name': 'Studio Wireless Headphones',
        'description': 'Active noise cancellation, 30-hour battery',
        'price': '199.00',
        'image': 'storefront/images/products/headphones.jpg',
    },
    {
        'name': 'Minimalist Leather Watch',
        'description': 'Stainless steel case, genuine leather strap',
        'price': '89.00',
        'image': 'storefront/images/products/watch.jpg',
    },
    {
        'name': 'Classic Court Sneakers',
        'description': 'Everyday comfort with a timeless silhouette',
        'price': '74.00',
        'image': 'storefront/images/products/sneakers.jpg',
    },
]


def landing(request):
    return render(request, 'storefront/landing.html', {'products': PRODUCTS})

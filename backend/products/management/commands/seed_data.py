from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Seed the database with sample kitchenware products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding sample data...')

        # Categories
        cats = [
            {'name': 'Cookware',           'slug': 'cookware',           'order': 1},
            {'name': 'Pressure Cookers',   'slug': 'pressure-cookers',   'order': 2},
            {'name': 'Storage',            'slug': 'storage',            'order': 3},
            {'name': 'Serving',            'slug': 'serving',            'order': 4},
        ]
        cat_objs = {}
        for c in cats:
            obj, _ = Category.objects.get_or_create(slug=c['slug'], defaults=c)
            cat_objs[c['slug']] = obj

        # Products
        products = [
            {
                'name': "Chef's Casserole Set",
                'description': 'Triple-layered 18/8 stainless steel with encapsulated base for even heat distribution. Oven and induction safe.',
                'category': cat_objs['cookware'],
                'price': 1299, 'original_price': 1799,
                'rating': 4.9, 'badge': 'Best Seller', 'order': 1,
            },
            {
                'name': 'Pressure Cooker 5L',
                'description': 'ISI-marked with safety valve, pressure indicator and bakelite handles. Induction-compatible. Suitable for daily cooking.',
                'category': cat_objs['pressure-cookers'],
                'price': 2199, 'original_price': None,
                'rating': 4.9, 'badge': 'Top Rated', 'order': 2,
            },
            {
                'name': 'Steel Tiffin Set (3 Tier)',
                'description': 'Leak-proof gasket seal, stackable design with locking clip. Dishwasher safe. Perfect for office or school.',
                'category': cat_objs['storage'],
                'price': 549, 'original_price': 699,
                'rating': 4.8, 'badge': 'Popular', 'order': 3,
            },
            {
                'name': 'Serving Bowl Set (6 pcs)',
                'description': 'Mirror-polished serving bowls in 3 sizes. Dishwasher safe. Perfect for every occasion from daily meals to parties.',
                'category': cat_objs['serving'],
                'price': 799, 'original_price': None,
                'rating': 4.7, 'badge': '', 'order': 4,
            },
            {
                'name': 'Kadai with Lid',
                'description': 'Deep wok-style kadai with glass lid. Tri-ply base for perfect heat retention. Induction and gas compatible.',
                'category': cat_objs['cookware'],
                'price': 1649, 'original_price': 1999,
                'rating': 4.8, 'badge': '', 'order': 5,
            },
            {
                'name': 'Steel Water Bottle 1L',
                'description': 'Double-wall vacuum insulated. Keeps water cold 24hrs, hot 12hrs. BPA-free lid. Leak-proof.',
                'category': cat_objs['storage'],
                'price': 449, 'original_price': None,
                'rating': 4.6, 'badge': 'New', 'order': 6,
            },
        ]

        for p in products:
            Product.objects.get_or_create(name=p['name'], defaults=p)

        self.stdout.write(self.style.SUCCESS(
            f'Done! Created {len(cats)} categories and {len(products)} products.'
        ))

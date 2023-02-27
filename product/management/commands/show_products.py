from django.core.management.base import BaseCommand, CommandError
from product.models import Product
from datetime import datetime

class Command(BaseCommand):
    help = 'prints the products in command line and can also update them'

    def add_arguments(self, parser):
        parser.add_argument('product_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print("these are the arguments got:")
        print(args, options)
        product_ids = options.get('product_id')
        if product_ids[0] != 0:
            products = list(Product.objects.filter(pk__in=product_ids).all())
        for product in products:
            print("*"*20)
            print(f"{product.name}- {product.description} \nprice:{product.price}")
            product.updated = datetime.now()
            product.save()
        print("*"*20)

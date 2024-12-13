import traceback
from django.core.management.base import BaseCommand
import csv
import datetime

from ...models import Products


class Command(BaseCommand):
    help = "Import products from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    
    def handle(self, *args, **kwargs):
        from django.utils.timezone import make_aware
        with open(kwargs['csv_file'], 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            products = []
            for row in reader:
                # {'id': '1', 'name': 'Option', 'category': 'Sports', 'price': '491.15', 'stock': '751', 'created_at': '2023-10-27T03:15:10'}
                try:
                    price = float(row['price']) if row['price'] else 0
                    stock = int(row['stock']) if row['stock'] else 0
                    products.append(Products(
                        id=row['id'],
                        name = row['name'],
                        category = row['category'],
                        price = price,
                        stock = stock,
                        # created_at = make_aware(datetime.datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%S')),
                        created_at = row['created_at']
                    ))
                    print(f'{row}')
                except Exception as e:
                    print(f'This row is causing error: {e}, Row - {row}')
                    continue
            # import ipdb; ipdb.set_trace()
            try:
                Products.objects.bulk_create(products)
                print(f'Successfully Imported')
            except Exception as e:
                print(f'Bulk Import Failed - {str(e)} {traceback.format_exc()}')
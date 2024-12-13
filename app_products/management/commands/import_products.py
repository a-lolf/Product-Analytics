import traceback
from django.core.management.base import BaseCommand
import csv

from ...models import Products


class Command(BaseCommand):
    help = "Import products from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    
    def handle(self, **options):
        file = options['csv_file']
        with open(file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            products = []
            for row in reader:
                try:
                    price = float(row['price']) if row['price'] else 0
                    stock = int(row['stock']) if row['stock'] else 0
                    products.append(Products(
                        id=row['id'],
                        name = row['name'],
                        category = row['category'],
                        price = price,
                        stock = stock,
                        created_at = row['created_at']
                    ))
                except Exception as e:
                    print(f'This row is causing error: {str(e)}, Row - {row}')
                    continue
            try:
                Products.objects.bulk_create(products)
                print(f'Successfully Imported')
            except Exception as e:
                print(f'Bulk Import Failed - {str(e)} {traceback.format_exc()}')
                
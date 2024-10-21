import csv
from django.core.management.base import BaseCommand
from calc.models import Customer

class Command(BaseCommand):
    help = 'Import student data from a CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')
    
    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] and row['age']:  
                    Customer.objects.create(
                        name=row['name'],
                        age=row['age']
                    )
            self.stdout.write(self.style.SUCCESS('Successfully imported customer data'))
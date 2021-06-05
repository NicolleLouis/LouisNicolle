from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(os.environ['RDS_DB_NAME'])
        print(os.environ['RDS_USERNAME'])
        print(os.environ['RDS_PASSWORD'])
        print(os.environ['RDS_HOSTNAME'])
        print(os.environ['RDS_PORT'])

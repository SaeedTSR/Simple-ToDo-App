from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

user = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not user.objects.filter(email='admin@admin.com').exists():
            user.objects.create_superuser(
                email='admin@admin.com',
                password='admin2000'
            )
        print('Superuser has been created.')
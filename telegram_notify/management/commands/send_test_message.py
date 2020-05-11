from django.core.management.base import BaseCommand
from telegram_notify.bot import send_test_message


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_test_message()

import uuid
from sqlite3 import OperationalError

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from notifications.models import Category
from notifications.utilities.local_data import LocalDataHandler


@receiver(post_migrate)
def load_initial_data(**kwargs):
    local_data_handler = LocalDataHandler()
    local_data_handler.load_categories()

from django.db import transaction

from ..models import User, LogHistory
import logging

logger = logging.getLogger(__name__)


def notify(message):
    """
    Notifies subscribed users via the appropriate channels based on the given message.

    This function retrieves the category from the given message and finds the users
    who are subscribed to that category. For each subscribed user, it determines the
    appropriate channel(s) for notification and creates a log history entry. The
    notification message is logged to the console.

    Parameters:
        message (GilaMessage): The GilaMessage object containing the notification details.

    Returns:
        None
    """
    log_history_objs = []

    category = message.category
    subscribed_users = User.objects.filter(subscribed__id=category.id).prefetch_related('channels')

    for user in subscribed_users:
        for channel in user.channels.all():
            log_history = LogHistory(user=user, channel=channel, message=message)
            log_history_objs.append(log_history)

            # Log the notification message to the console
            logger.info(f"Notified to {user.email} by {channel.type}, message: {message.message}")

    # Save the log_history objects in the DB
    with transaction.atomic():
        LogHistory.objects.bulk_create(log_history_objs)


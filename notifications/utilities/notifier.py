import logging

from notifications.utilities import local_data
from notifications.utilities.local_data import LocalDataHandler

logger = logging.getLogger(__name__)


def new_message_notify(message):
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
    category = message.category

    # Load users and categories
    local_data_handler = LocalDataHandler()
    local_data_handler.load_categories()
    local_data_handler.load_local_users()

    users = local_data_handler.get_subscribed_users(category)
    for user in users:
        print("User notified: {}:".format(user.name))
        user.send_notifications(message)

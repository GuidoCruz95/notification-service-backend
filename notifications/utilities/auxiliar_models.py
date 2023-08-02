from enum import Enum
from functools import wraps
from typing import List

from notifications.models import Category, LogHistory, GilaMessage


def log_notify(func):
    """
    Decorator function to log notifications.

    This decorator logs notifications by creating a LogHistory entry in the database.

    Args:
        func (function): The notification function to be decorated.

    Returns:
        function: The decorated notification function.
    """

    @wraps(func)
    def wrapper(self, user, message):
        """
        Wrapper function for the decorated notification function.

        Args:
            self: The instance of the class.
            user (User): The user to be notified.
            message (GilaMessage): The notification message.

        Returns:
            Any: The result of the original notification function.
        """
        gila_message = GilaMessage.objects.get(id=message.id)
        log_history = LogHistory(
            user=user,
            message=gila_message,
            channel_type=self.channel_type.value
        )
        log_history.save()
        print("Registered a new entry for LogHistory in the database.")
        return func(self, user, message)

    return wrapper


class ChannelType(Enum):
    """
    Enum representing the type of notification channels.
    """
    SMS = 'SMS'
    EMAIL = 'E-Mail'
    PUSH_NOTIFICATION = 'Push Notification'


class Channel:
    """
    Represents a notification channel associated with a category.

    Attributes:
        identifier (UUID): The unique identifier for the channel.
        channel_type (ChannelType): The type of the channel.
        description (str): A brief description of the channel.
    """

    def __init__(self, identifier, channel_type: ChannelType, description):
        self.identifier = identifier
        self.channel_type = channel_type
        self.description = description

    def __str__(self):
        return self.channel_type.value

    @log_notify
    def notify(self, user, message):
        """
        Notify using the specific notification channel.

        Args:
            user (User): The user to notify.
            message (str): The message to send via the channel.
        """
        raise NotImplementedError("Subclasses must implement notify function.")


class SMSChannel(Channel):
    """
    Represents an SMS notification channel.

    Attributes:
        phone_number (str): The phone number associated with the channel.
    """

    def __init__(self, identifier, channel_type: ChannelType, description):
        super().__init__(identifier, channel_type, description)
        self.phone_number = None

    def set_phone_number(self, phone_number):
        """
        Set the phone number associated with the SMS channel.

        Args:
            phone_number (str): The phone number to set.
        """
        self.phone_number = phone_number

    @log_notify
    def notify(self, user, message):
        """
        Notify using SMS.

        Args:
            user (User): The user to notify.
            message (str): The message to send via SMS.
        """
        print("Notified by SMS to: {}".format(self.phone_number))


class EmailChannel(Channel):
    """
    Represents an email notification channel.

    Attributes:
        email_address (str): The email address associated with the channel.
    """

    def __init__(self, identifier, channel_type: ChannelType, description):
        super().__init__(identifier, channel_type, description)
        self.email_address = None

    def set_email(self, email_address):
        """
        Set the email address associated with the email channel.

        Args:
            email_address (str): The email address to set.
        """
        self.email_address = email_address

    @log_notify
    def notify(self, user, message):
        """
        Notify using email.

        Args:
            user (User): The user to notify.
            message (str): The message to send via email.
        """
        print("Notified by Email to: {}".format(self.email_address))


class PushNotificationChannel(Channel):
    """
    Represents a push notification channel.

    Attributes:
        device_token (str): The device token associated with the channel.
    """

    def __init__(self, identifier, channel_type: ChannelType, description):
        super().__init__(identifier, channel_type, description)
        self.device_token = None

    def set_device_token(self, device_token):
        """
        Set the device token associated with the push notification channel.

        Args:
            device_token (str): The device token to set.
        """
        self.device_token = device_token

    @log_notify
    def notify(self, user, message):
        """
        Notify using push notification.

        Args:
            user (User): The user to notify.
            message (str): The message to send via push notification.
        """
        # Implement push notification logic here
        print("Notified by PushNotification to: {}".format(self.device_token))


class User:
    """
    Represents a user.

    Attributes:
        identifier (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        phone_number (int): The phone number of the user.
        subscribed_categories (List[Category]): A list of subscribed categories.
        channels (List[Channel]): A list of notification channels associated with the user.
    """

    def __init__(self, identifier, name, email, phone_number, categories=None, channels=None):
        self.identifier = identifier
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.subscribed_categories: [Category] = categories if categories is not None else []
        self.channels: [Channel] = channels if channels is not None else []

    def add_channel(self, channel: Channel):
        """
        Add a notification channel to the user's channels.

        Args:
            channel (Channel): The channel to add.
        """
        self.channels.append(channel)

    def subscribe_category(self, category: Category):
        """
        Subscribe the user to a category.

        Args:
            category (Category): The category to subscribe to.
        """
        self.subscribed_categories.append(category)

    def send_notifications(self, message):
        """
        Send notifications to the user using subscribed channels.

        Args:
            message (str): The message to send via notifications.
        """
        for user_channel in self.channels:
            user_channel.notify(self.name, message)

    def __str__(self):
        return self.name

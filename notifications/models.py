import uuid

from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    Represents a category for grouping messages.

    The Category model defines a category that can be used to group related messages.

    Attributes:
        id (UUIDField): The unique identifier for the category.
        name (CharField): The name of the category, limited to 30 characters.
        description (CharField): A brief description of the category, limited to 30 characters.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GilaMessage(models.Model):
    """
    Represents a message with an associated category.

    The GilaMessage model defines a message that is associated with a specific category.

    Attributes:
        id (UUIDField): The unique identifier for the gilaMessage.
        message (TextField): The content of the message, allowing unlimited characters.
        category (ForeignKey): A foreign key to the Category model, representing the associated category.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Channel(models.Model):
    """
    Represents a channel with an associated category.

    The Channel model defines a message that is associated with a specific category.

    Attributes:
        id (UUIDField): The unique identifier for the channel.
        name (TextField): The name of the channel.
        description (CharField): A brief description of the channel.
        type (CharField): The type of the channel (SMS, E-Mail, Push Notification).
        category (ForeignKey): A foreign key to the Category model, representing the associated category.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TYPE_CHOICES = (
        ('SMS', 'SMS'),
        ('E-Mail', 'E-Mail'),
        ('Push Notification', 'Push Notification'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.type


class User(models.Model):
    """
    Represents a user.

    The User model represents a user with a name, email, phone number, and related subscribed_categories.

    Attributes:
        id (UUIDField): The unique identifier for the user.
        name (CharField): The name of the user, limited to 35 characters.
        email (CharField): The email address of the user, limited to 35 characters.
        phone_number (IntegerField): The phone number of the user.
        subscribed (ManyToManyField): A many-to-many relationship with the Category model,
            representing the categories to which the user is subscribed.
        channels (ManyToManyField): A many-to-many relationship with the Channel model,
            representing the channels associated with the user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    phone_number = models.IntegerField()
    subscribed = models.ManyToManyField(Category)
    channels = models.ManyToManyField(Channel)

    def __str__(self):
        return self.name


class LogHistory(models.Model):
    """
    Represents a LogHistory.

    The LogHistory model represents a log entry with information about the user, channel, and message.

    Attributes:
        id (UUIDField): The unique identifier for the log history entry.
        time (DateTimeField): The date and time when the log entry was created. Default value is the current date and time.
        user (ForeignKey): A foreign key to the User model, representing the user associated with the log entry.
        channel (ForeignKey): A foreign key to the Channel model, representing the channel associated with the log entry.
        message (TextField): The content of the log entry, allowing unlimited characters.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return "Log ID: {id}, Time: {time}, User: {user}, Channel: {channel}".format(
            id=self.id,
            time=self.time,
            user=self.user,
            channel=self.channel
        )

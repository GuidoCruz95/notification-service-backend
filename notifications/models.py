import uuid
from django.db import models


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
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    phone_number = models.IntegerField()
    subscribed = models.ManyToManyField(Category)
    channels = models.ManyToManyField(Channel)

    def __str__(self):
        return self.name

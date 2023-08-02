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
    user = models.CharField(max_length=50)
    channel_type = models.CharField(max_length=50)
    message = models.ForeignKey(GilaMessage, on_delete=models.CASCADE)

    def __str__(self):
        return "Log ID: {id}, Time: {time}, User: {user}".format(
            id=self.id,
            time=self.time,
            user=self.user,
            channel_type=self.channel_type
        )

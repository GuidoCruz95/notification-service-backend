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


class Message(models.Model):
    """
    Represents a message with an associated category.

    The Message model defines a message that is associated with a specific category.

    Attributes:
        id (UUIDField): The unique identifier for the message.
        message (TextField): The content of the message, allowing unlimited characters.
        category (ForeignKey): A foreign key to the Category model, representing the associated category.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

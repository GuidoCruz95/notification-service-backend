from rest_framework import generics
from .models import Category, Message
from .serializers import CategorySerializer, MessageSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Category objects.

    The CategoryListCreateView is a generic view that handles listing all existing
    Category objects and creating new Category objects.

    Attributes:
        queryset (QuerySet): The queryset of Category objects to be listed.
        serializer_class (CategorySerializer): The serializer class to convert
            Category objects to JSON representation and vice versa.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Category object.

    The CategoryRetrieveUpdateDeleteView is a generic view that handles retrieving,
    updating, and deleting a specific Category object based on its primary key (id).

    Attributes:
        queryset (QuerySet): The queryset of Category objects from which to retrieve
            the specific Category object.
        serializer_class (CategorySerializer): The serializer class to convert
            Category objects to JSON representation and vice versa.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MessageListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Message objects.

    The MessageListCreateView is a generic view that handles listing all existing
    Message objects and creating new Message objects.

    Attributes:
        queryset (QuerySet): The queryset of Message objects to be listed.
        serializer_class (MessageSerializer): The serializer class to convert
            Message objects to JSON representation and vice versa.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Message object.

    The MessageRetrieveUpdateDeleteView is a generic view that handles retrieving,
    updating, and deleting a specific Message object based on its primary key (id).

    Attributes:
        queryset (QuerySet): The queryset of Message objects from which to retrieve
            the specific Message object.
        serializer_class (MessageSerializer): The serializer class to convert
            Message objects to JSON representation and vice versa.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

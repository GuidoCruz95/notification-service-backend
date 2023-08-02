from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Category, GilaMessage, LogHistory
from .serializers import CategorySerializer, MessageSerializer, LogHistorySerializer
from .utilities.notifier import new_message_notify


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
    queryset = GilaMessage.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save()
            new_message_notify(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    queryset = GilaMessage.objects.all()
    serializer_class = MessageSerializer


class LogHistoryViewSet(viewsets.ModelViewSet):
    """
    API viewset for listing users filtered by a specific category.

    The CategoryUsersViewSet is a viewset that provides a custom action for filtering users
    based on a specific category.

    Attributes:
        queryset (QuerySet): The queryset of User objects to be listed, retrieved, etc.
        serializer_class (UserSerializer): The serializer class to convert User objects to JSON representation and vice versa.
    """

    queryset = LogHistory.objects.all()
    serializer_class = LogHistorySerializer

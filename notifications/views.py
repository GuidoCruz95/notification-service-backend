from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, GilaMessage, User, LogHistory
from .serializers import CategorySerializer, MessageSerializer, UserSerializer, LogHistorySerializer
from .utilities.notifier import notify


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


class CategoryUsersViewSet(viewsets.ModelViewSet):
    """
    API viewset for listing users filtered by a specific category.

    The CategoryUsersViewSet is a viewset that provides a custom action for filtering users
    based on a specific category.

    Attributes:
        queryset (QuerySet): The queryset of User objects to be listed, retrieved, etc.
        serializer_class (UserSerializer): The serializer class to convert User objects to JSON representation and vice versa.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='category_users')
    def category_users(self, request):
        """
        Custom action to retrieve users filtered by a specific category.

        Args:
            request: The HTTP request.

        Returns:
            A list of users filtered by the specified category or all users if category_id is not provided.
            Returns a response with filtered users and status code 200 if successful.
            Returns a response with an error message and status code 400 if an invalid category_id is provided.
        """
        category_id = request.query_params.get('category_id')
        filtered_users = []
        if category_id:
            try:
                users = User.objects.filter(subscribed__id=category_id)
                serializer = UserSerializer(users, many=True)
                filtered_users = serializer.data
            except ValueError:
                return Response({"error": "Invalid category_id"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(filtered_users, status=status.HTTP_200_OK)


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
            notify(message)
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


class UserListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating User objects.

    The UserListCreateView is a generic view that handles listing all existing
    User objects and creating new User objects.

    Attributes:
        queryset (QuerySet): The queryset of User objects to be listed.
        serializer_class (UserSerializer): The serializer class to convert
            User objects to JSON representation and vice versa.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific User object.

    The UserRetrieveUpdateDeleteView is a generic view that handles retrieving,
    updating, and deleting a specific User object based on its primary key (id).

    Attributes:
        queryset (QuerySet): The queryset of User objects from which to retrieve
            the specific User object.
        serializer_class (UserSerializer): The serializer class to convert
            User objects to JSON representation and vice versa.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

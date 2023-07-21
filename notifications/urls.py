from django.urls import path

from .views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView, \
    UserListCreateView, UserRetrieveUpdateDeleteView, CategoryUsersViewSet, LogHistoryViewSet
from .views import MessageListCreateView, MessageRetrieveUpdateDeleteView

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'),

    # Message URLs
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<uuid:pk>/', MessageRetrieveUpdateDeleteView.as_view(), name='message-retrieve-update-delete'),

    # User URLs
    path('users/', UserListCreateView.as_view(), name='users-list-create'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='users-retrieve-update-delete'),
    path(
        'category-users/',
        CategoryUsersViewSet.as_view({'get': 'category_users'}),
        name='users-by-category-list'
    ),

    # Log History URLs
    path('log-history/', LogHistoryViewSet.as_view({'get': 'list'}), name='log-history-list'),
]

from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView
from .views import MessageListCreateView, MessageRetrieveUpdateDeleteView

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'),

    # Message URLs
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<uuid:pk>/', MessageRetrieveUpdateDeleteView.as_view(), name='message-retrieve-update-delete'),
]

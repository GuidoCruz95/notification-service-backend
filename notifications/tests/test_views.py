from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate

from ..models import Channel, Category, GilaMessage, User, LogHistory
from ..views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView, MessageListCreateView, \
    MessageRetrieveUpdateDeleteView, UserListCreateView, UserRetrieveUpdateDeleteView, LogHistoryViewSet


class CategoryViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Test Category', description='Test Description')

    def test_category_list_view(self):
        request = self.factory.get('/categories/')
        view = CategoryListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_create_view(self):
        data = {'name': 'New Category', 'description': 'New Description'}
        request = self.factory.post('/categories/', data, format='json')
        view = CategoryListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_retrieve_view(self):
        request = self.factory.get(f'/categories/{self.category.id}/')
        view = CategoryRetrieveUpdateDeleteView.as_view()
        response = view(request, pk=self.category.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MessageViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.message = GilaMessage.objects.create(message='Test Message', category=self.category)

    def test_message_list_view(self):
        request = self.factory.get('/messages/')
        view = MessageListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_create_view(self):
        data = {'message': 'New Message', 'category': self.category.id}
        request = self.factory.post('/messages/', data, format='json')
        view = MessageListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_message_retrieve_view(self):
        request = self.factory.get(f'/messages/{self.message.id}/')
        view = MessageRetrieveUpdateDeleteView.as_view()
        response = view(request, pk=self.message.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.channel = Channel.objects.create(type='SMS', description='SMS channel')
        self.user = User.objects.create(name='Test User', email='test@example.com', phone_number=1234567890)
        self.user.subscribed.add(self.category)
        self.user.channels.add(self.channel)

    def test_user_list_view(self):
        request = self.factory.get('/users/')
        view = UserListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create_view(self):
        data = {'name': 'New User', 'email': 'newuser@example.com', 'phone_number': 9876543210,
                'subscribed': [self.category.id], 'channels': [self.channel.id]}
        request = self.factory.post('/users/', data, format='json')
        view = UserListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_retrieve_view(self):
        request = self.factory.get(f'/users/{self.user.id}/')
        view = UserRetrieveUpdateDeleteView.as_view()
        response = view(request, pk=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LogHistoryViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.user = User.objects.create(name='Test User', email='test@example.com', phone_number=1234567890)
        self.channel = Channel.objects.create(type='SMS', description='Test Channel Description')
        self.log_history = LogHistory.objects.create(user=self.user, channel=self.channel, message='Test Log Message')

    def test_log_history_list_view(self):
        request = self.factory.get('/log-history/')
        view = LogHistoryViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


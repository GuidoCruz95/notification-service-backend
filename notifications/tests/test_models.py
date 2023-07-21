from django.test import TestCase
from notifications.models import Category, GilaMessage, Channel, User, LogHistory


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')

    def test_category_attributes(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'Test Description')

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), 'Test Category')


class GilaMessageModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.message = GilaMessage.objects.create(message='Test Message', category=self.category)

    def test_gila_message_attributes(self):
        self.assertEqual(self.message.message, 'Test Message')
        self.assertEqual(self.message.category, self.category)

    def test_gila_message_str_representation(self):
        self.assertEqual(str(self.message), 'Test Message')


class ChannelModelTestCase(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(type='SMS', description='Test Channel Description')

    def test_channel_attributes(self):
        self.assertEqual(self.channel.type, 'SMS')
        self.assertEqual(self.channel.description, 'Test Channel Description')

    def test_channel_str_representation(self):
        self.assertEqual(str(self.channel), 'SMS')


class UserModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.user = User.objects.create(name='Test User', email='test@example.com', phone_number=1234567890)

    def test_user_attributes(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.phone_number, 1234567890)

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'Test User')


class LogHistoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.user = User.objects.create(name='Test User', email='test@example.com', phone_number=1234567890)
        self.channel = Channel.objects.create(type='SMS', description='Test Channel Description')
        self.log_history = LogHistory.objects.create(user=self.user, channel=self.channel, message='Test Log Message')

    def test_log_history_attributes(self):
        self.assertEqual(self.log_history.user, self.user)
        self.assertEqual(self.log_history.channel, self.channel)
        self.assertEqual(self.log_history.message, 'Test Log Message')

    def test_log_history_str_representation(self):
        expected_str = f"Log ID: {self.log_history.id}, Time: {self.log_history.time}, User: {self.user}, Channel: {self.channel}"
        self.assertEqual(str(self.log_history), expected_str)

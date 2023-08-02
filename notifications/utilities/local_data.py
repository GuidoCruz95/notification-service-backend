from notifications.models import Category
from notifications.utilities.auxiliar_models import User, SMSChannel, EmailChannel, ChannelType, PushNotificationChannel


class LocalDataHandler:
    """
    LocalDataHandler class is responsible for managing and loading local data for testing purposes.

    Attributes:
        users (List[User]): A list of User objects containing user information and subscriptions.
        categories (QuerySet): A QuerySet containing Category objects representing message categories.
    """

    def __init__(self):
        self.users: [User] = []
        self.categories = None

    def load_categories(self):
        """
        Load predefined categories or create them if they don't exist in the database.
        """
        self.categories = Category.objects.all()

        sport_id = "b0b691d0-4e2f-4b47-8e61-579c72e4c4f2"
        try:
            sport_category = Category.objects.get(id=sport_id)
        except Category.DoesNotExist:
            sport_category = Category.objects.create(id=sport_id, name='sport', description='Default Description')
            sport_category.save()

        finance_id = "6f7e6f3b-e9b2-4e44-9f3b-1ec25d19aa8e"
        try:
            finance_category = Category.objects.get(id=finance_id)
        except Category.DoesNotExist:
            finance_category = Category.objects.create(id=finance_id, name='Finance', description='Default Description')
            finance_category.save()

        movies_id = "58d3bea3-d5e0-4b47-9ac4-27836e73e6eb"
        try:
            movies_category = Category.objects.get(id=movies_id)
        except Category.DoesNotExist:
            movies_category = Category.objects.create(id=movies_id, name='Movies', description='Default Description')
            movies_category.save()

    def load_local_users(self):
        """
        Load local user data with predefined channels and subscriptions.
        """
        josh = User(100, "Josh", "josh@mal.com", 454545, self.categories)
        sms_channel = SMSChannel(2000, ChannelType.SMS, "description")
        sms_channel.set_phone_number(josh.phone_number)
        josh.add_channel(sms_channel)

        harrison = User(101, "Harrison", "harrison@mal.com", 454545, self.categories[1:])
        email_channel = EmailChannel(2001, ChannelType.EMAIL, "description")
        email_channel.set_email(harrison.email)
        sms_channel = SMSChannel(2005, ChannelType.SMS, "description")
        sms_channel.set_phone_number(harrison.phone_number)
        harrison.add_channel(email_channel)
        harrison.add_channel(sms_channel)

        dan = User(102, "Dan", "dan@mal.com", 454545, [])
        self.users.append(josh)
        self.users.append(harrison)
        self.users.append(dan)
        self.print_users_subscriptions()

    def print_users_subscriptions(self):
        """
        Print users' subscriptions and channel configurations.
        """
        for user in self.users:
            print("user: '{}' is subscribed to: '{}' with channels: {}".format(
                user.name,
                [item.name for item in user.subscribed_categories],
                [item.channel_type.value for item in user.channels])
            )

    def get_subscribed_users(self, category):
        """
        Get a list of users subscribed to a specific category.

        Args:
            category (Category): The category to check for subscriptions.

        Returns:
            List[User]: A list of User objects subscribed to the given category.
        """
        users = []
        for item in self.users:
            if category in item.subscribed_categories:
                users.append(item)
        return users

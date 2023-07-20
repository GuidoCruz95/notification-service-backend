from rest_framework import serializers
from .models import Category, GilaMessage, Channel, User


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    The CategorySerializer is used to convert Category model instances to JSON
    representation and vice versa. It provides a straightforward way to serialize
    and deserialize Category objects.

    Attributes:
        Meta: A nested class that defines the serializer's behavior and configuration.
            model (Category): The Django model associated with the serializer.
            fields (list or '__all__'): The fields to include in the serialized representation
                of Category objects. If '__all__' is used, all fields of the model will be included.
    """

    class Meta:
        model = Category
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.

    The MessageSerializer is used to convert Message model instances to JSON
    representation and vice versa. It provides a straightforward way to serialize
    and deserialize Message objects.

    Attributes:
        Meta: A nested class that defines the serializer's behavior and configuration.
            model (Message): The Django model associated with the serializer.
            fields (list or '__all__'): The fields to include in the serialized representation
                of Message objects. If '__all__' is used, all fields of the model will be included.
    """

    class Meta:
        model = GilaMessage
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    """
    Serializer for the Channel model.

    The ChannelSerializer is used to convert Channel model instances to JSON
    representation and vice versa. It provides a straightforward way to serialize
    and deserialize Channel objects.

    Attributes:
        Meta: A nested class that defines the serializer's behavior and configuration.
            model (Channel): The Django model associated with the serializer.
            fields (list or '__all__'): The fields to include in the serialized representation
                of Channel objects. If '__all__' is used, all fields of the model will be included.
    """

    class Meta:
        model = Channel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    The UserSerializer is used to convert User model instances to JSON
    representation and vice versa. It provides a straightforward way to serialize
    and deserialize User objects.

    Attributes:
        Meta: A nested class that defines the serializer's behavior and configuration.
            model (User): The Django model associated with the serializer.
            fields (list or '__all__'): The fields to include in the serialized representation
                of User objects. If '__all__' is used, all fields of the model will be included.
    """

    class Meta:
        model = User
        fields = '__all__'

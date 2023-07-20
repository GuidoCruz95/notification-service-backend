from rest_framework import serializers
from .models import Category, Message


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
        model = Message
        fields = '__all__'
